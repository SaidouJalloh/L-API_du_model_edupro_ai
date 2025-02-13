# New code avec de news fonctionalitées
from redis import Redis
import os
import json
import requests
import hashlib
import toml
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS
from functools import lru_cache
# from redis import Redis  # Optionnel si tu veux un cache Redis
from utils import convert_duration_to_hours  # Assurez-vous que ce fichier existe

# Charger les variables d'environnement
load_dotenv()

# Charger les secrets depuis secrets.toml
secrets_path = "C:/Users/Imam Said/Desktop/Edu_pro_IA/.streamlit/secrets.toml"

if os.path.exists(secrets_path):
    secrets = toml.load(secrets_path)
    os.environ.setdefault("GEMINI_API_KEY", secrets.get("GEMINI_API_KEY", ""))
    os.environ.setdefault("GEMINI_API_URL", secrets.get("GEMINI_API_URL", ""))
    os.environ.setdefault("API_SECRET_KEY", secrets.get("API_SECRET_KEY", ""))

# Initialisation de Flask
app = Flask(__name__)
CORS(app, origins=["https://mon-frontend.com"])  # Restriction des accès

# Protection contre l'abus d'API
# limiter = Limiter(get_remote_address, app=app, default_limits=["10 per minute"])

limiter = Limiter(key_func=get_remote_address, storage_uri="redis://redis:6379/0")
limiter.init_app(app)

# limiter = Limiter(get_remote_address, app=app, key_func=get_remote_address, storage_uri="redis://redis:6379/0")


# Chargement des clés API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = os.getenv("GEMINI_API_URL")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")

# Vérification des valeurs chargées (clés masquées)
print(f"GEMINI_API_KEY: {GEMINI_API_KEY[:4]}****")
print(f"GEMINI_API_URL: {GEMINI_API_URL}")
print(f"API_SECRET_KEY: {'****' if API_SECRET_KEY else 'Non défini'}")

# Cache en mémoire pour éviter des requêtes redondantes
cache = {}

# Option Redis (décommente si besoin)
redis_client = Redis(host="localhost", port=6379, db=0)

def get_cached_response(hash_input):
    return redis_client.get(hash_input)


def generate_course_prompt(inputs):
    """ Génère le prompt pour l'API Gemini """
    duration_hours = convert_duration_to_hours(inputs['duration'], inputs['duration_unit'])

    return f"""En tant qu'expert en formation, génère un programme de formation avec la structure JSON suivante.

Input:
- Sujet: {inputs['subject']}
- Format: {inputs['format_type']}
- Niveau: {inputs['level']}
- Durée: {duration_hours} heures
- Langue: {inputs['language']}
- Contexte: {inputs['context']}
{f"- Prérequis: {inputs['prerequisites']}" if inputs.get('prerequisites') else ''}

Format JSON à respecter:
{{
    "title": "titre_formation",
    "keywords": ["mot_cle1", "mot_cle2", "mot_cle3"],
    "description": "description_formation",
    "objectives": ["objectif1", "objectif2", "objectif3"],
    "target_audience": "public_cible",
    "expected_results": ["resultat1", "resultat2", "resultat3"],
    "prerequisites": ["prerequis1", "prerequis2"],
    "chapters": [
        {{"identifier": "Module1",
        "title": "titre_module",
        "duration": "durée_du_module",
        "description": "description_module",
        "content": [
            {{"type": "video",
            "title": "titre_video",
            "description": "description_video",
            "url": ""}},
            {{"type": "text",
            "title": "titre_texte",
            "description": "description_texte"}}
        ],
        "quiz": {{"title": "titre_quiz",
            "description": "description_quiz",
            "questions": [
                {{"question": "Question?",
                "options": ["Option1", "Option2", "Option3", "Option4"],
                "correct_answer": 0,
                "explanation": "Explication"}}
            ]
        }}
        }}
    ]
}}

IMPORTANT:
1. Contenu adapté au niveau {inputs['level']}
2. Contenu en {inputs['language']}
3. Retourner uniquement le JSON, sans texte avant ou après
4. Chaque module doit avoir 2-3 contenus (video/text/audio)
5. Quiz après chaque module avec 2-3 questions"""


def check_api_key():
    """ Vérifie si la clé API est correcte """
    api_key = request.headers.get("Authorization")
    if not api_key or api_key != f"Bearer {API_SECRET_KEY}":
        return jsonify({"error": "Unauthorized"}), 401
    return None


@lru_cache(maxsize=100)  # Limite à 100 entrées
def get_cached_response(hash_input):
    return cache.get(hash_input)


@app.route('/generate_course', methods=['POST'])
@limiter.limit("5 per minute")
def generate_course():
    """Génère un programme de formation basé sur un sujet donné"""
    
    auth_error = check_api_key()
    if auth_error:
        return auth_error  # Renvoie l'erreur si la clé API est invalide

    try:
        if not request.is_json:
            return jsonify({"error": "Invalid request, JSON expected"}), 400

        inputs = request.json
        required_fields = ["subject", "format_type", "level", "duration", "duration_unit", "language", "context"]

        if not all(field in inputs for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400

        # Vérifier si cette requête a déjà été traitée (cache)
        hash_input = hashlib.sha256(json.dumps(inputs, sort_keys=True).encode()).hexdigest()
        cached_data = get_cached_response(hash_input)
        if cached_data:
            return jsonify({"cached": True, "data": cached_data})

        prompt = generate_course_prompt(inputs)

        headers = {"Content-Type": "application/json"}
        payload = {"contents": [{"parts": [{"text": prompt}]}]}

        response = requests.post(f"{GEMINI_API_URL}?key={GEMINI_API_KEY}", json=payload, headers=headers)

        if response.status_code != 200:
            return jsonify({"error": "Erreur lors de la requête à Gemini"}), 500

        try:
            response_data = response.json()
        except ValueError:
            return jsonify({"error": "Réponse invalide de l'API Gemini"}), 500

        # Stocker en cache
        cache[hash_input] = response_data
        return jsonify(response_data)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Erreur API Gemini : {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
