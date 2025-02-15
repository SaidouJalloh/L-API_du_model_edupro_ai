
# # V1 qui marche bien
# def generate_course_prompt(inputs):
#     """
#     Génère le prompt pour l'API Gemini
#     """
#     return f"""Tu es un expert en création de formation. Génère un programme de formation en respectant STRICTEMENT le format JSON suivant, sans aucun texte avant ou après. La réponse doit être un JSON valide.

# Input:
# - Sujet: {inputs['subject']}
# - Format: {inputs['format_type']}
# - Niveau: {inputs['level']}
# - Durée: {inputs['duration']} heures
# - Langue: {inputs['language']}
# - Contexte: {inputs['context']}
# {f"- Prérequis: {inputs['prerequisites']}" if inputs.get('prerequisites') else ''}

# Format JSON STRICT à respecter :
# {{
#     "title": "titre_formation",
#     "keywords": [
#         "mot_cle1",
#         "mot_cle2",
#         "mot_cle3"
#     ],
#     "description": "description_formation",
#     "objectives": [
#         "objectif1",
#         "objectif2",
#         "objectif3"
#     ],
#     "target_audience": "public_cible",
#     "expected_results": [
#         "resultat1",
#         "resultat2",
#         "resultat3"
#     ],
#     "prerequisites": [
#         "prerequis1",
#         "prerequis2"
#     ],
#     "chapters": [
#         {{
#             "identifier": "Module1",
#             "title": "titre_module",
#             "xp": "20",
#             "description": "description_module",
#             "content": [
#                 {{
#                     "type": "video",
#                     "title": "titre_video"
#                 }},
#                 {{
#                     "type": "image",
#                     "title": "titre_image"
#                 }},
#                 {{
#                     "type": "audio",
#                     "title": "titre_audio"
#                 }},
#                 {{
#                     "type": "text",
#                     "title": "titre_texte"
#                 }},
#                 {{
#                     "type": "document",
#                     "title": "titre_document"
#                 }},
#                 {{
#                     "type": "quiz",
#                     "title": "titre_quiz"
#                 }}
#             ]
#         }}
#     ]
# }}

# IMPORTANT:
# 1. Respecte STRICTEMENT la structure JSON fournie
# 2. Ne mets aucun texte avant ou après le JSON
# 3. Assure-toi que toutes les accolades et guillemets sont correctement fermés
# 4. Le contenu doit être en {inputs['language']}
# 5. Adapte le contenu au niveau {inputs['level']}
# 6. Ne change pas les clés du JSON, seulement les valeurs"""




# V1 avec de news fonctionnalités
# prompt_template.py

# def convert_duration_to_hours(duration, unit):
#     """Convertit la durée en heures selon l'unité choisie"""
#     conversions = {
#         "heures": 1,
#         "jours": 24,
#         "semaines": 24 * 7,
#         "mois": 24 * 30
#     }
#     return duration * conversions[unit]

# def generate_course_prompt(inputs):
#     """
#     Génère le prompt pour l'API Gemini
#     """
#     return f"""En tant qu'expert en formation, génère un programme de formation avec la structure JSON suivante.

# Input:
# - Sujet: {inputs['subject']}
# - Format: {inputs['format_type']}
# - Niveau: {inputs['level']}
# - Durée: {inputs['duration']} {inputs['duration_unit']}
# - Langue: {inputs['language']}
# - Contexte: {inputs['context']}
# {f"- Prérequis: {inputs['prerequisites']}" if inputs.get('prerequisites') else ''}

# Format JSON à respecter:
# {{
#     "title": "titre_formation",
#     "keywords": ["mot_cle1", "mot_cle2", "mot_cle3"],
#     "description": "description_formation",
#     "objectives": ["objectif1", "objectif2", "objectif3"],
#     "target_audience": "public_cible",
#     "expected_results": ["resultat1", "resultat2", "resultat3"],
#     "prerequisites": ["prerequis1", "prerequis2"],
#     "chapters": [
#         {{
#             "identifier": "Module1",
#             "title": "titre_module",
#             "duration": "durée_du_module",
#             "description": "description_module",
#             "content": [
#                 {{
#                     "type": "video",
#                     "title": "titre_video",
#                     "description": "description_video",
#                     "url": ""
#                 }},
#                 {{
#                     "type": "text",
#                     "title": "titre_texte",
#                     "description": "description_texte"
#                 }}
#             ],
#             "quiz": {{
#                 "title": "titre_quiz",
#                 "description": "description_quiz",
#                 "questions": [
#                     {{
#                         "question": "Question?",
#                         "options": ["Option1", "Option2", "Option3", "Option4"],
#                         "correct_answer": 0,
#                         "explanation": "Explication"
#                     }}
#                 ]
#             }}
#         }}
#     ]
# }}

# IMPORTANT:
# 1. Contenu adapté au niveau {inputs['level']}
# 2. Contenu en {inputs['language']}
# 3. Retourner uniquement le JSON, sans texte avant ou après
# 4. Chaque module doit avoir 2-3 contenus (video/text/audio)
# 5. Quiz après chaque module avec 2-3 questions"""