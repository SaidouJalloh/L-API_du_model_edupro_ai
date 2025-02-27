
# V1 qui marche mais pas très flexible
# from flask import Flask, request, jsonify
# import google.generativeai as genai
# from utils import generate_course_prompt, convert_duration_to_hours
# import os
# from dotenv import load_dotenv
# from flask_cors import CORS

# # Charger les variables d'environnement
# load_dotenv()

# app = Flask(__name__)
# CORS(app)

# # Configuration des variables d'environnement
# app.config['SECRET_KEY'] = os.getenv('API_SECRET_KEY')

# # Documentation de l'API (accessible via /docs)
# SWAGGER_DOCS = {
#     "swagger": "2.0",
#     "info": {
#         "title": "API Générateur de Cours",
#         "description": "API pour générer des plans de cours structurés",
#         "version": "1.0"
#     },
#     "paths": {
#         "/generate-course": {
#             "post": {
#                 "description": "Génère un plan de cours structuré",
#                 "parameters": [
#                     {
#                         "name": "body",
#                         "in": "body",
#                         "required": True,
#                         "schema": {
#                             "type": "object",
#                             "properties": {
#                                 "subject": {"type": "string"},
#                                 "format_type": {"type": "string"},
#                                 "level": {"type": "string"},
#                                 "duration": {"type": "number"},
#                                 "duration_unit": {"type": "string"},
#                                 "language": {"type": "string"},
#                                 "context": {"type": "string"},
#                                 "prerequisites": {"type": "string"}
#                             }
#                         }
#                     }
#                 ],
#                 "responses": {
#                     "200": {"description": "Plan de cours généré avec succès"},
#                     "400": {"description": "Erreur dans les paramètres"},
#                     "500": {"description": "Erreur serveur"}
#                 }
#             }
#         }
#     }
# }

# # Configuration de l'API Gemini
# genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
# model = genai.GenerativeModel('gemini-pro')


# @app.route('/docs', methods=['GET'])
# def get_docs():
#     """Retourne la documentation de l'API"""
#     return jsonify(SWAGGER_DOCS)

# @app.route('/health', methods=['GET'])
# def health_check():
#     """Route de vérification de l'état de l'API"""
#     return jsonify({
#         'status': 'healthy',
#         'message': 'Service is running'
#     }), 200

# @app.route('/generate-course', methods=['POST'])
# def generate_course():
#     """Route principale pour la génération de cours"""
#     try:
#         # Validation des données d'entrée
#         required_fields = ['subject', 'format_type', 'level', 'duration', 
#                          'duration_unit', 'language', 'context']
        
#         data = request.get_json()
        
#         if not data:
#             return jsonify({
#                 'error': 'No data provided'
#             }), 400

#         # Vérification des champs requis
#         missing_fields = [field for field in required_fields if field not in data]
#         if missing_fields:
#             return jsonify({
#                 'error': f'Missing required fields: {", ".join(missing_fields)}'
#             }), 400

#         # Génération du prompt
#         prompt = generate_course_prompt(data)

#         # Appel à l'API Gemini
#         response = model.generate_content(prompt)
        
#         # Vérification et nettoyage de la réponse
#         if response.text:
#             try:
#                 # Retourner la réponse JSON directement
#                 return response.text, 200
#             except Exception as e:
#                 return jsonify({
#                     'error': 'Invalid JSON response from model',
#                     'details': str(e)
#                 }), 500
#         else:
#             return jsonify({
#                 'error': 'Empty response from model'
#             }), 500

#     except Exception as e:
#         return jsonify({
#             'error': 'Internal server error',
#             'details': str(e)
#         }), 500

# @app.errorhandler(404)
# def not_found(error):
#     return jsonify({
#         'error': 'Route not found'
#     }), 404

# @app.errorhandler(500)
# def internal_error(error):
#     return jsonify({
#         'error': 'Internal server error'
#     }), 500

# if __name__ == '__main__':
#     port = int(os.getenv('PORT', 8282))
#     app.run(debug=True, host='0.0.0.0', port=port)






# V2 plus flexible
import os
import logging
import json
import re
import hashlib
from flask import Flask, request, jsonify
import google.generativeai as genai
from utils import (
    generate_course_structure_prompt,
    generate_course_complete_prompt,
    generate_chapter_content_prompt,
    generate_quiz_prompt,
    generate_exercise_prompt,
    generate_resource_prompt,
    generate_video_transcript_prompt,
    generate_certification_prompt
)
from dotenv import load_dotenv
from flask_cors import CORS
from functools import lru_cache
from typing import Dict, Optional, Any, List

# Configuration du logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Chargement des variables d'environnement
load_dotenv()
app.config['SECRET_KEY'] = os.getenv('API_SECRET_KEY')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY non définie dans les variables d'environnement")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro')

# Configuration du cache LRU
CACHE_SIZE = 100
cache_hits = 0
cache_misses = 0

@lru_cache(maxsize=CACHE_SIZE)
def get_cached_response(hash_key: str) -> Optional[Dict]:
    """Cache LRU pour stocker les résultats"""
    return None

def set_cached_response(hash_key: str, response: Dict) -> None:
    """Stocke la réponse dans le cache"""
    global cache_misses
    cache_misses += 1
    get_cached_response.cache_clear()
    get_cached_response(hash_key)  # Enregistre la clé
    get_cached_response.cache_info = lambda: {'response': response}  # Stocke la réponse

def clean_json_response(response_text: str) -> Dict:
    """Nettoie et valide la réponse JSON du modèle."""
    try:
        # Supprimer les délimiteurs markdown et le texte avant/après
        clean_text = re.sub(r"```json|```", "", response_text).strip()
        
        # Trouver le premier accolade ouvrante et la dernière fermante
        start_idx = clean_text.find("{")
        end_idx = clean_text.rfind("}")
        
        if start_idx == -1 or end_idx == -1:
            raise ValueError("No valid JSON object found in response")
        
        clean_text = clean_text[start_idx:end_idx + 1]
        
        # Gérer les virgules trailing
        clean_text = re.sub(r',\s*}', '}', clean_text)
        clean_text = re.sub(r',\s*]', ']', clean_text)
        
        # Parse le JSON
        try:
            return json.loads(clean_text)
        except json.JSONDecodeError:
            # Si échec, essayer de nettoyer davantage
            clean_text = clean_text.replace('\n', '').replace('\r', '')
            return json.loads(clean_text)
            
    except Exception as e:
        logger.error(f"Error cleaning JSON response: {str(e)}")
        logger.error(f"Original text: {response_text[:500]}...")
        raise

def generate_ai_content(prompt: str, temperature: float = 0.2) -> Dict:
    """
    Génère du contenu via l'API Gemini et nettoie la réponse.
    
    Args:
        prompt: Le prompt à envoyer à l'API
        temperature: Niveau de créativité (0.0 à 1.0)
        
    Returns:
        La réponse nettoyée au format JSON
    """
    try:
        generation_config = {
            "temperature": temperature,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
        }
        
        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            }
        ]
        
        response = model.generate_content(
            prompt,
            generation_config=generation_config,
            safety_settings=safety_settings
        )
        
        return clean_json_response(response.text)
    
    except Exception as e:
        logger.error(f"Error in generate_ai_content: {str(e)}")
        raise

def generate_course_structure(data: Dict) -> Dict:
    """
    Génère uniquement la structure du cours sans contenu détaillé.
    
    Args:
        data: Les paramètres du cours
        
    Returns:
        La structure du cours au format JSON
    """
    prompt = generate_course_structure_prompt(data)
    
    # Génération avec une température basse pour plus de cohérence
    return generate_ai_content(prompt, temperature=0.1)

def generate_full_course(data: Dict) -> Dict:
    """
    Génère un cours complet avec tout le contenu, chapitres, quiz, etc.
    
    Args:
        data: Les paramètres du cours
        
    Returns:
        Le cours complet au format JSON
    """
    prompt = generate_course_complete_prompt(data)
    
    # Génération avec une température moyenne pour un bon équilibre
    return generate_ai_content(prompt, temperature=0.3)

def generate_chapter(chapter_info: Dict, course_info: Dict = None) -> Dict:
    """
    Génère le contenu détaillé d'un chapitre.
    
    Args:
        chapter_info: Informations sur le chapitre
        course_info: Informations sur le cours (optionnel)
        
    Returns:
        Le chapitre enrichi au format JSON
    """
    prompt = generate_chapter_content_prompt(chapter_info, course_info)
    
    # Génération avec une température moyenne
    return generate_ai_content(prompt, temperature=0.3)

def generate_quiz(chapter_info: Dict, course_info: Dict = None) -> Dict:
    """
    Génère un quiz pour un chapitre.
    
    Args:
        chapter_info: Informations sur le chapitre
        course_info: Informations sur le cours (optionnel)
        
    Returns:
        Le quiz au format JSON
    """
    prompt = generate_quiz_prompt(chapter_info, course_info)
    
    # Génération avec une température basse pour plus de cohérence
    return generate_ai_content(prompt, temperature=0.2)

def generate_exercise(chapter_info: Dict, course_info: Dict = None) -> Dict:
    """
    Génère un exercice pour un chapitre.
    
    Args:
        chapter_info: Informations sur le chapitre
        course_info: Informations sur le cours (optionnel)
        
    Returns:
        L'exercice au format JSON
    """
    prompt = generate_exercise_prompt(chapter_info, course_info)
    
    # Génération avec une température moyenne
    return generate_ai_content(prompt, temperature=0.3)

def generate_course_resources(course_info: Dict) -> Dict:
    """
    Génère des ressources complémentaires pour un cours.
    
    Args:
        course_info: Informations sur le cours
        
    Returns:
        Les ressources au format JSON
    """
    prompt = generate_resource_prompt(course_info)
    
    # Génération avec une température moyenne-haute pour plus de variété
    return generate_ai_content(prompt, temperature=0.4)

def generate_video_content(video_info: Dict, course_info: Dict = None) -> Dict:
    """
    Génère une transcription de vidéo.
    
    Args:
        video_info: Informations sur la vidéo
        course_info: Informations sur le cours (optionnel)
        
    Returns:
        La transcription au format JSON
    """
    prompt = generate_video_transcript_prompt(video_info, course_info)
    
    # Génération avec une température plus haute pour un style naturel
    return generate_ai_content(prompt, temperature=0.5)

def generate_certification(course_info: Dict) -> Dict:
    """
    Génère une structure de certification pour un cours.
    
    Args:
        course_info: Informations sur le cours
        
    Returns:
        La certification au format JSON
    """
    prompt = generate_certification_prompt(course_info)
    
    # Génération avec une température moyenne
    return generate_ai_content(prompt, temperature=0.3)

def generate_structured_content(data: Dict, mode: str = "complete") -> Dict:
    """
    Génère le contenu structuré selon le mode choisi, avec cache.
    
    Args:
        data: Les paramètres du cours
        mode: Le mode de génération ("structure", "complete", "progressive")
        
    Returns:
        Le contenu généré au format JSON
    """
    try:
        global cache_hits
        
        # Création d'une clé de cache unique basée sur les données et le mode
        cache_key = f"{mode}_{hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()}"
        
        # Vérification du cache
        cached_result = get_cached_response(cache_key)
        if cached_result and hasattr(get_cached_response, 'cache_info'):
            cache_hits += 1
            logger.info(f"Cache hit! Total hits: {cache_hits}")
            return get_cached_response.cache_info()['response']

        # Génération selon le mode choisi
        if mode == "structure":
            # Génération de la structure seule
            result = generate_course_structure(data)
        
        elif mode == "complete":
            # Génération du cours complet en une fois
            result = generate_full_course(data)
        
        elif mode == "progressive":
            # Génération progressive : structure puis chapitres un par un
            structure = generate_course_structure(data)
            
            # Génération du contenu pour chaque chapitre
            for i, chapter in enumerate(structure.get('data', {}).get('chapters', [])):
                logger.info(f"Generating content for chapter {i+1}: {chapter['title']}")
                
                # Génération du contenu du chapitre
                chapter_content = generate_chapter(chapter, data)
                
                # Génération du quiz pour ce chapitre
                quiz = generate_quiz(chapter, data)
                
                # Génération d'un exercice pour ce chapitre
                exercise = generate_exercise(chapter, data)
                
                # Mise à jour du chapitre avec le contenu généré
                if 'contents' not in chapter_content:
                    chapter_content['contents'] = []
                
                # Ajout des éléments générés au chapitre
                structure['data']['chapters'][i] = chapter_content
                
                # Si le quiz n'est pas déjà dans les contents
                quiz_exists = any(item.get('type') == 'QUIZ' for item in chapter_content.get('contents', []))
                if not quiz_exists and quiz:
                    chapter_content['contents'].append(quiz)
                
                # Si l'exercice n'est pas déjà dans les contents
                exercise_exists = any(item.get('type') == 'EXERCISE' for item in chapter_content.get('contents', []))
                if not exercise_exists and exercise:
                    chapter_content['contents'].append(exercise)
            
            # Génération des ressources complémentaires
            resources = generate_course_resources(data)
            if resources and 'resources' in resources:
                structure['data']['resources'] = resources['resources']
            
            # Génération de la certification
            certification = generate_certification(data)
            if certification and 'certification' in certification:
                structure['data']['certification'] = certification['certification']
            
            result = structure
        else:
            raise ValueError(f"Mode de génération non reconnu: {mode}")

        # Mise en cache du résultat
        set_cached_response(cache_key, result)
        return result

    except Exception as e:
        logger.error(f"Error in generate_structured_content: {str(e)}")
        raise

# Routes API

@app.route('/generate-course', methods=['POST'])
def generate_course():
    """
    Route principale pour la génération de cours avec différents modes.
    
    Modes disponibles:
    - structure: génère uniquement la structure du cours
    - complete: génère le cours complet en une requête
    - progressive: génère la structure puis enrichit progressivement (recommandé pour les grands cours)
    """
    try:
        required_fields = ['subject', 'format_type', 'level', 'duration', 'duration_unit', 'language', 'context']
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({'error': f'Missing required fields: {", ".join(missing_fields)}'}), 400
        
        # Récupération du mode de génération (par défaut: complete)
        mode = request.args.get('mode', 'complete')
        if mode not in ['structure', 'complete', 'progressive']:
            return jsonify({'error': f'Invalid generation mode: {mode}. Must be one of: structure, complete, progressive'}), 400

        json_response = generate_structured_content(data, mode)
        
        # Si le mode est structure, on renvoie uniquement la structure
        if mode == 'structure' and 'data' in json_response:
            # S'assurer que les chapitres n'ont pas de contenu
            if 'chapters' in json_response['data']:
                for chapter in json_response['data']['chapters']:
                    if 'contents' in chapter:
                        del chapter['contents']
        
        return jsonify(json_response), 200

    except Exception as e:
        logger.exception("Internal server error")
        return jsonify({'error': str(e)}), 500

@app.route('/generate-chapter', methods=['POST'])
def generate_chapter_route():
    """
    Endpoint pour générer un chapitre complet 
    (contenu + quiz + exercice)
    """
    try:
        data = request.get_json()
        if not data or 'chapter_info' not in data:
            return jsonify({'error': 'Missing chapter_info in request'}), 400

        chapter_info = data['chapter_info']
        course_info = data.get('course_info', None)
        
        # Génération du contenu du chapitre
        chapter_content = generate_chapter(chapter_info, course_info)
        
        # Si le client demande également le quiz et l'exercice
        include_quiz = data.get('include_quiz', True)
        include_exercise = data.get('include_exercise', True)
        
        if include_quiz:
            # Génération du quiz associé à ce chapitre
            quiz = generate_quiz(chapter_info, course_info)
            
            # Ajout du quiz aux contenus du chapitre
            if 'contents' not in chapter_content:
                chapter_content['contents'] = []
            
            # Vérifier si un quiz existe déjà
            quiz_exists = any(item.get('type') == 'QUIZ' for item in chapter_content.get('contents', []))
            if not quiz_exists and quiz:
                chapter_content['contents'].append(quiz)
        
        if include_exercise:
            # Génération de l'exercice associé à ce chapitre
            exercise = generate_exercise(chapter_info, course_info)
            
            # Ajout de l'exercice aux contenus du chapitre
            if 'contents' not in chapter_content:
                chapter_content['contents'] = []
            
            # Vérifier si un exercice existe déjà
            exercise_exists = any(item.get('type') == 'EXERCISE' for item in chapter_content.get('contents', []))
            if not exercise_exists and exercise:
                chapter_content['contents'].append(exercise)
        
        return jsonify(chapter_content), 200

    except Exception as e:
        logger.exception("Error generating chapter")
        return jsonify({'error': str(e)}), 500

@app.route('/generate-quiz', methods=['POST'])
def generate_quiz_route():
    """Endpoint pour générer uniquement un quiz"""
    try:
        data = request.get_json()
        if not data or 'chapter_info' not in data:
            return jsonify({'error': 'Missing chapter_info for quiz generation'}), 400

        chapter_info = data['chapter_info']
        course_info = data.get('course_info', None)
        
        quiz_content = generate_quiz(chapter_info, course_info)
        return jsonify(quiz_content), 200

    except Exception as e:
        logger.exception("Error generating quiz")
        return jsonify({'error': str(e)}), 500

@app.route('/generate-exercise', methods=['POST'])
def generate_exercise_route():
    """Endpoint pour générer uniquement un exercice"""
    try:
        data = request.get_json()
        if not data or 'chapter_info' not in data:
            return jsonify({'error': 'Missing chapter_info for exercise generation'}), 400

        chapter_info = data['chapter_info']
        course_info = data.get('course_info', None)
        
        exercise_content = generate_exercise(chapter_info, course_info)
        return jsonify(exercise_content), 200

    except Exception as e:
        logger.exception("Error generating exercise")
        return jsonify({'error': str(e)}), 500

@app.route('/generate-resources', methods=['POST'])
def generate_resources_route():
    """Endpoint pour générer des ressources complémentaires"""
    try:
        data = request.get_json()
        if not data or 'course_info' not in data:
            return jsonify({'error': 'Missing course_info for resources generation'}), 400

        course_info = data['course_info']
        
        resources = generate_course_resources(course_info)
        return jsonify(resources), 200

    except Exception as e:
        logger.exception("Error generating resources")
        return jsonify({'error': str(e)}), 500

@app.route('/generate-video-transcript', methods=['POST'])
def generate_video_transcript_route():
    """Endpoint pour générer une transcription de vidéo"""
    try:
        data = request.get_json()
        if not data or 'video_info' not in data:
            return jsonify({'error': 'Missing video_info for transcript generation'}), 400

        video_info = data['video_info']
        course_info = data.get('course_info', None)
        
        transcript = generate_video_content(video_info, course_info)
        return jsonify(transcript), 200

    except Exception as e:
        logger.exception("Error generating video transcript")
        return jsonify({'error': str(e)}), 500

@app.route('/generate-certification', methods=['POST'])
def generate_certification_route():
    """Endpoint pour générer une structure de certification"""
    try:
        data = request.get_json()
        if not data or 'course_info' not in data:
            return jsonify({'error': 'Missing course_info for certification generation'}), 400
            
        course_info = data['course_info']
        
        certification = generate_certification(course_info)
        return jsonify(certification), 200

    except Exception as e:
        logger.exception("Error generating certification")
        return jsonify({'error': str(e)}), 500

@app.route('/update-chapter', methods=['PUT'])
def update_chapter_route():
    """Endpoint pour mettre à jour un chapitre existant"""
    try:
        data = request.get_json()
        if not data or 'chapter_id' not in data or 'course_id' not in data:
            return jsonify({'error': 'Missing chapter_id or course_id for chapter update'}), 400
            
        chapter_id = data['chapter_id']
        course_id = data['course_id']
        updates = data.get('updates', {})
        
        # Ici, vous implémenteriez la logique pour récupérer et mettre à jour le chapitre
        # dans votre système de stockage (base de données, fichier JSON, etc.)
        
        # Pour l'instant, nous simulons une mise à jour réussie
        return jsonify({
            'success': True,
            'message': f'Chapter {chapter_id} in course {course_id} updated successfully',
            'updated_fields': list(updates.keys())
        }), 200

    except Exception as e:
        logger.exception("Error updating chapter")
        return jsonify({'error': str(e)}), 500

@app.route('/add-content-to-chapter', methods=['POST'])
def add_content_to_chapter_route():
    """Endpoint pour ajouter un nouveau contenu à un chapitre existant"""
    try:
        data = request.get_json()
        if not data or 'chapter_id' not in data or 'content_type' not in data:
            return jsonify({'error': 'Missing chapter_id or content_type'}), 400
            
        chapter_id = data['chapter_id']
        content_type = data['content_type'].upper()  # TEXT, VIDEO, AUDIO, EXERCISE, QUIZ
        
        # Validation du type de contenu
        valid_types = ['TEXT', 'VIDEO', 'AUDIO', 'EXERCISE', 'QUIZ']
        if content_type not in valid_types:
            return jsonify({'error': f'Invalid content_type. Must be one of: {", ".join(valid_types)}'}), 400
        
        # Récupération des informations de contexte
        chapter_info = data.get('chapter_info', {'id': chapter_id})
        course_info = data.get('course_info', None)
        
        # Génération du contenu selon le type demandé
        if content_type == 'QUIZ':
            new_content = generate_quiz(chapter_info, course_info)
        elif content_type == 'EXERCISE':
            new_content = generate_exercise(chapter_info, course_info)
        else:
            # Pour les autres types (TEXT, VIDEO, AUDIO), nous générons un contenu approprié
            # Cette partie nécessiterait des fonctions spécifiques pour chaque type
            # Pour l'instant, nous retournons un modèle simple
            new_content = {
                "id": f"{chapter_id}-{content_type.lower()}-new",
                "title": f"Nouveau contenu {content_type.lower()}",
                "type": content_type,
                "chapter_id": chapter_id
            }
        
        return jsonify({
            'success': True,
            'new_content': new_content
        }), 201

    except Exception as e:
        logger.exception(f"Error adding {data.get('content_type', 'unknown')} content to chapter")
        return jsonify({'error': str(e)}), 500

@app.route('/cache-stats', methods=['GET'])
def get_cache_stats():
    """Endpoint pour obtenir les statistiques du cache"""
    total = cache_hits + cache_misses
    return jsonify({
        'hits': cache_hits,
        'misses': cache_misses,
        'hit_ratio': cache_hits / total if total > 0 else 0,
        'cache_info': str(get_cached_response.cache_info())
    })

@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint pour vérifier l'état de l'API"""
    return jsonify({
        'status': 'healthy',
        'version': '1.0.0',
        'api': 'Course Generator API',
        'model': 'gemini-1.5-pro'
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8282))
    logger.info(f"Starting server on port {port}")
    app.run(debug=True, host='0.0.0.0', port=port)