

# V1 code qui marche mais pas très flexible
# Derniere version avec le format adapter
# def convert_duration_to_hours(duration, unit):
#     """Convertit la durée en heures selon l'unité choisie"""
#     conversions = {
#         "heures": 1,
#         "jours": 24,
#         "semaines": 24 * 7,
#         "mois": 24 * 30
#     }
#     return duration * conversions.get(unit, 1)
# def generate_course_prompt(inputs):
#     """Génère le prompt pour l'API avec une structure JSON enrichie et un contenu pédagogique détaillé"""
#     duration_hours = convert_duration_to_hours(inputs['duration'], inputs['duration_unit'])
    
#     # Calculer la répartition du temps par chapitre
#     time_per_chapter = duration_hours / 4  # Pour 4 chapitres minimum
    
#     return f"""
# En tant qu'expert pédagogique, crée un programme de formation professionnel et engageant suivant la structure JSON fournie.

# CONTEXTE ET PARAMÈTRES:
# - Sujet: {inputs['subject']}
# - Format: {inputs['format_type']}
# - Niveau: {inputs['level']}
# - Durée totale: {duration_hours} heures ({time_per_chapter} heures par chapitre)
# - Langue: {inputs['language']}
# - Public cible: {inputs['context']}
# {f"- Prérequis techniques: {inputs['prerequisites']}" if inputs.get('prerequisites') else ''}

# DIRECTIVES PÉDAGOGIQUES:
# 1. Structure d'apprentissage:
#    - Progression logique des concepts (du simple au complexe)
#    - Équilibre entre théorie (40%) et pratique (60%)
#    - Alternance entre contenus didactiques et exercices d'application
#    - Points de validation réguliers des acquis

# 2. Pour chaque chapitre:
#    - Introduction claire des objectifs d'apprentissage
#    - Contenu théorique structuré et illustré
#    - Au moins 2 exemples concrets par concept
#    - 1 cas pratique tiré du monde réel
#    - Exercices progressifs avec corrections détaillées
#    - Quiz de validation avec feedback personnalisé
#    - Synthèse des points clés

# 3. Types de contenus à intégrer:
#    - Texte: définitions, explications, études de cas
#    - Vidéo: démonstrations, tutoriels (5-10 minutes)
#    - Audio: synthèses, points clés à retenir
#    - Infographies: schémas explicatifs, mindmaps
#    - Exercices interactifs: simulations, mises en situation
#    - Ressources complémentaires: lectures, outils, templates

# 4. Évaluation et progression:
#    - Objectifs SMART pour chaque module
#    - Critères de réussite explicites
#    - Auto-évaluation progressive
#    - Feedback constructif et personnalisé
#    - Parcours de remédiation si nécessaire

# 5. Adaptation au niveau {inputs['level']}:
#    - Débutant: fondamentaux, vocabulaire, concepts de base
#    - Intermédiaire: approfondissement, cas pratiques complexes
#    - Avancé: expertise, innovation, meilleures pratiques

# FORMAT JSON À RESPECTER:
# {{
#     "data": {{
#         "id": "id_formation",
#         "title": "titre_formation",
#         "description": "description_formation",
#         "duration": "00:00:00",
#         "total_duration": {duration_hours},
#         "duration_unit": "hours",
#         "keywords": {{
#             "key-1": "mot_cle1",
#             "key-2": "mot_cle2",
#             "key-3": "mot_cle3"
#         }},
#         "learning_objectives": "objectifs_apprentissage",
#         "expected_outcomes": {{
#             "outcome-1": "resultat1",
#             "outcome-2": "resultat2",
#             "outcome-3": "resultat3"
#         }},
#         "target_audience": "public_cible",
#         "prerequisites": {{
#             "pre-1": "prerequis1",
#             "pre-2": "prerequis2"
#         }},
#         "theme": "{inputs['subject']}",
#         "level": "{inputs['level']}",
#         "language": "{inputs['language']}",
#         "course_format": "{inputs['format_type']}",
#         "chapters": [
#             {{
#                 "id": "chapter-1",
#                 "title": "titre_chapitre",
#                 "order": 1,
#                 "duration": "00:00:00",
#                 "xp": 10,
#                 "quiz_id": "quiz-1",
#                 "description": "description_chapitre",
#                 "contents": [
#                     {{
#                         "id": "content-1",
#                         "title": "titre_contenu",
#                         "lesson": "<p>introduction_section</p>",
#                         "order": 1,
#                         "type": "TEXT",
#                         "duration": "00:00:00",
#                         "chapter_id": "chapter-1",
#                         "title_chapter": "titre_chapitre",
#                         "media_type": "TEXT",
#                         "media": null
#                     }},
#                     {{
#                         "id": "content-2",
#                         "title": "titre_contenu",
#                         "lesson": "<p>introduction_section</p>",
#                         "order": 2,
#                         "type": "TEXT",
#                         "duration": "00:00:00",
#                         "chapter_id": "chapter-1",
#                         "title_chapter": "titre_chapitre",
#                         "media_type": "TEXT",
#                         "media": null
#                     }},
#                     {{
#                         "id": "exercise-1",
#                         "title": "Exercice pratique",
#                         "order": 3,
#                         "type": "EXERCISE",
#                         "duration": "00:00:00",
#                         "content": {{
#                             "description": "description_exercice",
#                             "steps": [
#                                 "etape1",
#                                 "etape2",
#                                 "etape3"
#                             ],
#                             "expected_output": "resultat_attendu",
#                             "hints": [
#                                 "indice1",
#                                 "indice2"
#                             ]
#                         }}
#                     }},
#                     {{
#                         "id": "quiz-1",
#                         "title": "Quiz du chapitre",
#                         "order": 4,
#                         "type": "QUIZ",
#                         "duration": "00:00:00",
#                         "questions": [
#                             {{
#                                 "id": "q1",
#                                 "question": "Question?",
#                                 "options": [
#                                     {{
#                                         "id": "a",
#                                         "text": "Option1",
#                                         "explanation": "Explication pour Option1"
#                                     }},
#                                     {{
#                                         "id": "b",
#                                         "text": "Option2",
#                                         "explanation": "Explication pour Option2"
#                                     }}
#                                 ],
#                                 "answer": "a",
#                                 "explanation": "Explication détaillée de la réponse correcte"
#                             }},
#                             {{
#                                 "id": "q2",
#                                 "question": "Question?",
#                                 "options": [
#                                     {{
#                                         "id": "a",
#                                         "text": "Option1",
#                                         "explanation": "Explication pour Option1"
#                                     }},
#                                     {{
#                                         "id": "b",
#                                         "text": "Option2",
#                                         "explanation": "Explication pour Option2"
#                                     }}
#                                 ],
#                                 "answer": "a",
#                                 "explanation": "Explication détaillée de la réponse correcte"
#                             }}
#                         ]
#                     }}
#                 ]
#             }},
#             {{
#                 "id": "chapter-2",
#                 "title": "titre_chapitre",
#                 "order": 2,
#                 "duration": "00:00:00",
#                 "xp": 10,
#                 "quiz_id": "quiz-2",
#                 "description": "description_chapitre",
#                 "contents": [
#                     {{
#                         "id": "content-3",
#                         "title": "titre_contenu",
#                         "lesson": "<p>introduction_section</p>",
#                         "order": 1,
#                         "type": "TEXT",
#                         "duration": "00:00:00",
#                         "chapter_id": "chapter-2",
#                         "title_chapter": "titre_chapitre",
#                         "media_type": "TEXT",
#                         "media": null
#                     }},
#                     {{
#                         "id": "content-4",
#                         "title": "titre_contenu",
#                         "lesson": "<p>introduction_section</p>",
#                         "order": 2,
#                         "type": "TEXT",
#                         "duration": "00:00:00",
#                         "chapter_id": "chapter-2",
#                         "title_chapter": "titre_chapitre",
#                         "media_type": "TEXT",
#                         "media": null
#                     }},
#                     {{
#                         "id": "exercise-2",
#                         "title": "Exercice pratique",
#                         "order": 3,
#                         "type": "EXERCISE",
#                         "duration": "00:00:00",
#                         "content": {{
#                             "description": "description_exercice",
#                             "steps": [
#                                 "etape1",
#                                 "etape2",
#                                 "etape3"
#                             ],
#                             "expected_output": "resultat_attendu",
#                             "hints": [
#                                 "indice1",
#                                 "indice2"
#                             ]
#                         }}
#                     }},
#                     {{
#                         "id": "quiz-2",
#                         "title": "Quiz du chapitre",
#                         "order": 4,
#                         "type": "QUIZ",
#                         "duration": "00:00:00",
#                         "questions": [
#                             {{
#                                 "id": "q1",
#                                 "question": "Question?",
#                                 "options": [
#                                     {{
#                                         "id": "a",
#                                         "text": "Option1",
#                                         "explanation": "Explication pour Option1"
#                                     }},
#                                     {{
#                                         "id": "b",
#                                         "text": "Option2",
#                                         "explanation": "Explication pour Option2"
#                                     }}
#                                 ],
#                                 "answer": "a",
#                                 "explanation": "Explication détaillée de la réponse correcte"
#                             }},
#                             {{
#                                 "id": "q2",
#                                 "question": "Question?",
#                                 "options": [
#                                     {{
#                                         "id": "a",
#                                         "text": "Option1",
#                                         "explanation": "Explication pour Option1"
#                                     }},
#                                     {{
#                                         "id": "b",
#                                         "text": "Option2",
#                                         "explanation": "Explication pour Option2"
#                                     }}
#                                 ],
#                                 "answer": "a",
#                                 "explanation": "Explication détaillée de la réponse correcte"
#                             }}
#                         ]
#                     }}
#                 ]
#             }},
#             {{
#                 "id": "chapter-3",
#                 "title": "titre_chapitre",
#                 "order": 3,
#                 "duration": "00:00:00",
#                 "xp": 10,
#                 "quiz_id": "quiz-3",
#                 "description": "description_chapitre",
#                 "contents": [
#                     {{
#                         "id": "content-5",
#                         "title": "titre_contenu",
#                         "lesson": "<p>introduction_section</p>",
#                         "order": 1,
#                         "type": "TEXT",
#                         "duration": "00:00:00",
#                         "chapter_id": "chapter-3",
#                         "title_chapter": "titre_chapitre",
#                         "media_type": "TEXT",
#                         "media": null
#                     }},
#                     {{
#                         "id": "content-6",
#                         "title": "titre_contenu",
#                         "lesson": "<p>introduction_section</p>",
#                         "order": 2,
#                         "type": "TEXT",
#                         "duration": "00:00:00",
#                         "chapter_id": "chapter-3",
#                         "title_chapter": "titre_chapitre",
#                         "media_type": "TEXT",
#                         "media": null
#                     }},
#                     {{
#                         "id": "exercise-3",
#                         "title": "Exercice pratique",
#                         "order": 3,
#                         "type": "EXERCISE",
#                         "duration": "00:00:00",
#                         "content": {{
#                             "description": "description_exercice",
#                             "steps": [
#                                 "etape1",
#                                 "etape2",
#                                 "etape3"
#                             ],
#                             "expected_output": "resultat_attendu",
#                             "hints": [
#                                 "indice1",
#                                 "indice2"
#                             ]
#                         }}
#                     }},
#                     {{
#                         "id": "quiz-3",
#                         "title": "Quiz du chapitre",
#                         "order": 4,
#                         "type": "QUIZ",
#                         "duration": "00:00:00",
#                         "questions": [
#                             {{
#                                 "id": "q1",
#                                 "question": "Question?",
#                                 "options": [
#                                     {{
#                                         "id": "a",
#                                         "text": "Option1",
#                                         "explanation": "Explication pour Option1"
#                                     }},
#                                     {{
#                                         "id": "b",
#                                         "text": "Option2",
#                                         "explanation": "Explication pour Option2"
#                                     }}
#                                 ],
#                                 "answer": "a",
#                                 "explanation": "Explication détaillée de la réponse correcte"
#                             }},
#                             {{
#                                 "id": "q2",
#                                 "question": "Question?",
#                                 "options": [
#                                     {{
#                                         "id": "a",
#                                         "text": "Option1",
#                                         "explanation": "Explication pour Option1"
#                                     }},
#                                     {{
#                                         "id": "b",
#                                         "text": "Option2",
#                                         "explanation": "Explication pour Option2"
#                                     }}
#                                 ],
#                                 "answer": "a",
#                                 "explanation": "Explication détaillée de la réponse correcte"
#                             }}
#                         ]
#                     }}
#                 ]
#             }},
#             {{
#                 "id": "chapter-4",
#                 "title": "titre_chapitre",
#                 "order": 4,
#                 "duration": "00:00:00",
#                 "xp": 10,
#                 "quiz_id": "quiz-4",
#                 "description": "description_chapitre",
#                 "contents": [
#                     {{
#                         "id": "content-7",
#                         "title": "titre_contenu",
#                         "lesson": "<p>introduction_section</p>",
#                         "order": 1,
#                         "type": "TEXT",
#                         "duration": "00:00:00",
#                         "chapter_id": "chapter-4",
#                         "title_chapter": "titre_chapitre",
#                         "media_type": "TEXT",
#                         "media": null
#                     }},
#                     {{
#                         "id": "content-8",
#                         "title": "titre_contenu",
#                         "lesson": "<p>introduction_section</p>",
#                         "order": 2,
#                         "type": "TEXT",
#                         "duration": "00:00:00",
#                         "chapter_id": "chapter-4",
#                         "title_chapter": "titre_chapitre",
#                         "media_type": "TEXT",
#                         "media": null
#                     }},
#                     {{
#                         "id": "exercise-4",
#                         "title": "Exercice pratique",
#                         "order": 3,
#                         "type": "EXERCISE",
#                         "duration": "00:00:00",
#                         "content": {{
#                             "description": "description_exercice",
#                             "steps": [
#                                 "etape1",
#                                 "etape2",
#                                 "etape3"
#                             ],
#                             "expected_output": "resultat_attendu",
#                             "hints": [
#                                 "indice1",
#                                 "indice2"
#                             ]
#                         }}
#                     }},
#                     {{
#                         "id": "quiz-4",
#                         "title": "Quiz du chapitre",
#                         "order": 4,
#                         "type": "QUIZ",
#                         "duration": "00:00:00",
#                         "questions": [
#                             {{
#                                 "id": "q1",
#                                 "question": "Question?",
#                                 "options": [
#                                     {{
#                                         "id": "a",
#                                         "text": "Option1",
#                                         "explanation": "Explication pour Option1"
#                                     }},
#                                     {{
#                                         "id": "b",
#                                         "text": "Option2",
#                                         "explanation": "Explication pour Option2"
#                                     }}
#                                 ],
#                                 "answer": "a",
#                                 "explanation": "Explication détaillée de la réponse correcte"
#                             }},
#                             {{
#                                 "id": "q2",
#                                 "question": "Question?",
#                                 "options": [
#                                     {{
#                                         "id": "a",
#                                         "text": "Option1",
#                                         "explanation": "Explication pour Option1"
#                                     }},
#                                     {{
#                                         "id": "b",
#                                         "text": "Option2",
#                                         "explanation": "Explication pour Option2"
#                                     }}
#                                 ],
#                                 "answer": "a",
#                                 "explanation": "Explication détaillée de la réponse correcte"
#                             }}
#                         ]
#                     }}
#                 ]
#             }}
#         ],
#         "cover": "cover-image.png",
#         "presentation_video": {{
#             "url": "https://youtu.be/video-id",
#             "type": "video",
#             "description": "description_video",
#             "transcript": "transcription_video"
#         }},
#         "resources": [
#             {{
#                 "id": "resource-1",
#                 "title": "titre_ressource",
#                 "type": "type_ressource",
#                 "url": "url_ressource",
#                 "description": "description_ressource"
#             }}
#         ],
#         "certification": {{
#             "available": true,
#             "title": "titre_certification",
#             "description": "description_certification",
#             "requirements": [
#                 "exigence1",
#                 "exigence2"
#             ]
#         }}
#     }}
# }}

# le contenu que tu dois generer doit etre au format json,surtout j'insiste sur le fait que tu dois retourner uniquement le json sans texte avant ou apres
# 1. Contenu adapté au niveau {inputs['level']}
# 2. Contenu en {inputs['language']}
# 3. Retourner uniquement le JSON, sans texte avant ou après
# 4. Chaque chapitre doit avoir:
#    - Une description détaillée
#    - Des objectifs d'apprentissage spécifiques
#    - Au moins 2 contenus de type TEXT avec structure complète
#    -au moins 1 contenus de type video
#    -au moins 1 contenus de type audio
#    - Un exercice pratique
#    - Un quiz avec 3-4 questions et explications
# 5. Générer au moins 4 chapitres selon la durée spécifiée
# 6. Inclure des ressources supplémentaires pertinentes
# 7. Adapter la difficulté du contenu et des exercices au niveau spécifié
# EXIGENCES DE QUALITÉ:
# 1. Contenu:
#    - Précision technique et factuelle
#    - Sources et références vérifiables
#    - Exemples concrets et actualisés
#    - Terminologie professionnelle adaptée

# 2. Pédagogie:
#    - Instructions claires et détaillées
#    - Progression logique des apprentissages
#    - Interactivité et engagement
#    - Évaluation continue des acquis

# 3. Format:
#    - Structure JSON valide et complète
#    - Durées adaptées au format et niveau
#    - Médias variés et pertinents
#    - Ressources téléchargeables utiles

# 4. Validation:
#    - Critères de réussite explicites
#    - Tests de connaissances réguliers
#    - Exercices pratiques notés
#    - Certification avec prérequis clairs

# RETOURNER UNIQUEMENT LE JSON GÉNÉRÉ, SANS TEXTE AVANT OU APRÈS"""




# V2 optimiser et flexible
# utils.py - Version améliorée
import json
from typing import Dict, Any, List

def convert_duration_to_hours(duration, unit):
    """Convertit la durée en heures selon l'unité choisie"""
    conversions = {
        "heures": 1,
        "jours": 24,
        "semaines": 24 * 7,
        "mois": 24 * 30
    }
    return duration * conversions.get(unit, 1)

def generate_course_structure_prompt(inputs: Dict) -> str:
    """
    Génère un prompt optimisé pour créer la structure du cours sans contenu détaillé.
    Idéal pour obtenir rapidement un squelette de cours.
    """
    duration_hours = convert_duration_to_hours(inputs['duration'], inputs['duration_unit'])
    
    return f"""
En tant qu'expert pédagogique, crée la structure complète d'un programme de formation sans le contenu détaillé.

CONTEXTE ET PARAMÈTRES:
- Sujet: {inputs['subject']}
- Format: {inputs['format_type']}
- Niveau: {inputs['level']}
- Durée totale: {duration_hours} heures 
- Langue: {inputs['language']}
- Public cible: {inputs['context']}
{f"- Prérequis techniques: {inputs['prerequisites']}" if inputs.get('prerequisites') else ''}

FORMAT JSON À RETOURNER EXACTEMENT:
{{
    "data": {{
        "id": "cours-{inputs['subject'].lower().replace(' ', '-')}",
        "title": "Titre pertinent et accrocheur",
        "description": "Description détaillée et engageante du programme",
        "duration": "00:00:00",
        "total_duration": {duration_hours},
        "duration_unit": "hours",
        "keywords": {{
            "key-1": "mot-clé principal",
            "key-2": "mot-clé secondaire",
            "key-3": "mot-clé spécifique",
            "key-4": "mot-clé technique",
            "key-5": "mot-clé sectoriel"
        }},
        "learning_objectives": "Objectifs d'apprentissage principaux (phrase synthétique)",
        "expected_outcomes": {{
            "outcome-1": "1. Premier résultat attendu ✅ détail 1 ✅ détail 2 ✅ détail 3",
            "outcome-2": "2. Deuxième résultat attendu ✅ détail 1 ✅ détail 2 ✅ détail 3",
            "outcome-3": "3. Troisième résultat attendu ✅ détail 1 ✅ détail 2 ✅ détail 3"
        }},
        "target_audience": "Description précise du public cible",
        "prerequisites": {{
            "pre-1": "Prérequis généraux sous forme de paragraphe",
            "pre-2": "1. Premier prérequis spécifique ✅ détail 1 ✅ détail 2 ✅ détail 3",
            "pre-3": "2. Deuxième prérequis spécifique ✅ détail 1 ✅ détail 2 ✅ détail 3"
        }},
        "theme": "{inputs['subject']}",
        "level": "{inputs['level']}",
        "language": "{inputs['language']}",
        "course_format": "{inputs['format_type']}",
        "chapters": [
            {{
                "id": "chapter-1",
                "title": "Titre du premier chapitre",
                "order": 1,
                "duration": "XX:XX:XX",
                "xp": 10,
                "description": "Description précise du contenu du chapitre",
                "cover": null
            }},
            {{
                "id": "chapter-2",
                "title": "Titre du deuxième chapitre",
                "order": 2,
                "duration": "XX:XX:XX",
                "xp": 15,
                "description": "Description précise du contenu du chapitre",
                "cover": null
            }}
            // Ajouter d'autres chapitres selon la durée totale
        ],
        "cover": null,
        "presentation_video": {{
            "url": "",
            "type": "video",
            "description": "",
            "transcript": ""
        }}
    }}
}}

EXIGENCES:
1. Créer 4 à 8 chapitres selon la durée totale ({duration_hours} heures) du cours
2. Assigner une durée logique à chaque chapitre (format XX:XX:XX)
3. Maintenir une progression pédagogique cohérente entre les chapitres
4. Adapter la complexité et le vocabulaire au niveau {inputs['level']}
5. Rédiger tout le contenu en {inputs['language']}

RETOURNER UNIQUEMENT LE JSON GÉNÉRÉ, SANS TEXTE AVANT OU APRÈS"""

def generate_course_complete_prompt(inputs: Dict) -> str:
    """Génère le prompt pour l'API avec une structure JSON enrichie et un contenu pédagogique détaillé"""
    duration_hours = convert_duration_to_hours(inputs['duration'], inputs['duration_unit'])
    
    # Calculer la répartition du temps par chapitre
    time_per_chapter = duration_hours / 4  # Pour 4 chapitres minimum
    
    return f"""
En tant qu'expert pédagogique, crée un programme de formation professionnel et engageant suivant la structure JSON fournie.

CONTEXTE ET PARAMÈTRES:
- Sujet: {inputs['subject']}
- Format: {inputs['format_type']}
- Niveau: {inputs['level']}
- Durée totale: {duration_hours} heures ({time_per_chapter} heures par chapitre)
- Langue: {inputs['language']}
- Public cible: {inputs['context']}
{f"- Prérequis techniques: {inputs['prerequisites']}" if inputs.get('prerequisites') else ''}

DIRECTIVES PÉDAGOGIQUES:
1. Structure d'apprentissage:
   - Progression logique des concepts (du simple au complexe)
   - Équilibre entre théorie (40%) et pratique (60%)
   - Alternance entre contenus didactiques et exercices d'application
   - Points de validation réguliers des acquis

2. Pour chaque chapitre:
   - Introduction claire des objectifs d'apprentissage
   - Contenu théorique structuré et illustré
   - Au moins 2 exemples concrets par concept
   - 1 cas pratique tiré du monde réel
   - Exercices progressifs avec corrections détaillées
   - Quiz de validation avec feedback personnalisé
   - Synthèse des points clés

3. Types de contenus à intégrer:
   - Texte: définitions, explications, études de cas
   - Vidéo: démonstrations, tutoriels (5-10 minutes)
   - Audio: synthèses, points clés à retenir
   - Infographies: schémas explicatifs, mindmaps
   - Exercices interactifs: simulations, mises en situation
   - Ressources complémentaires: lectures, outils, templates

4. Évaluation et progression:
   - Objectifs SMART pour chaque module
   - Critères de réussite explicites
   - Auto-évaluation progressive
   - Feedback constructif et personnalisé
   - Parcours de remédiation si nécessaire

5. Adaptation au niveau {inputs['level']}:
   - Débutant: fondamentaux, vocabulaire, concepts de base
   - Intermédiaire: approfondissement, cas pratiques complexes
   - Avancé: expertise, innovation, meilleures pratiques

FORMAT JSON À RESPECTER:
{{
    "data": {{
        "id": "id_formation",
        "title": "titre_formation",
        "description": "description_formation",
        "duration": "00:00:00",
        "total_duration": {duration_hours},
        "duration_unit": "hours",
        "keywords": {{
            "key-1": "mot_cle1",
            "key-2": "mot_cle2",
            "key-3": "mot_cle3"
        }},
        "learning_objectives": "objectifs_apprentissage",
        "expected_outcomes": {{
            "outcome-1": "resultat1",
            "outcome-2": "resultat2",
            "outcome-3": "resultat3"
        }},
        "target_audience": "public_cible",
        "prerequisites": {{
            "pre-1": "prerequis1",
            "pre-2": "prerequis2"
        }},
        "theme": "{inputs['subject']}",
        "level": "{inputs['level']}",
        "language": "{inputs['language']}",
        "course_format": "{inputs['format_type']}",
        "chapters": [
            {{
                "id": "chapter-1",
                "title": "titre_chapitre",
                "order": 1,
                "duration": "00:00:00",
                "xp": 10,
                "quiz_id": "quiz-1",
                "description": "description_chapitre",
                "contents": [
                    {{
                        "id": "content-1",
                        "title": "titre_contenu",
                        "lesson": "<p>introduction_section</p>",
                        "order": 1,
                        "type": "TEXT",
                        "duration": "00:00:00",
                        "chapter_id": "chapter-1",
                        "title_chapter": "titre_chapitre",
                        "media_type": "TEXT",
                        "media": null
                    }},
                    {{
                        "id": "content-2",
                        "title": "titre_contenu",
                        "lesson": "<p>introduction_section</p>",
                        "order": 2,
                        "type": "TEXT",
                        "duration": "00:00:00",
                        "chapter_id": "chapter-1",
                        "title_chapter": "titre_chapitre",
                        "media_type": "TEXT",
                        "media": null
                    }},
                    {{
                        "id": "exercise-1",
                        "title": "Exercice pratique",
                        "order": 3,
                        "type": "EXERCISE",
                        "duration": "00:00:00",
                        "content": {{
                            "description": "description_exercice",
                            "steps": [
                                "etape1",
                                "etape2",
                                "etape3"
                            ],
                            "expected_output": "resultat_attendu",
                            "hints": [
                                "indice1",
                                "indice2"
                            ]
                        }}
                    }},
                    {{
                        "id": "quiz-1",
                        "title": "Quiz du chapitre",
                        "order": 4,
                        "type": "QUIZ",
                        "duration": "00:00:00",
                        "questions": [
                            {{
                                "id": "q1",
                                "question": "Question?",
                                "options": [
                                    {{
                                        "id": "a",
                                        "text": "Option1",
                                        "explanation": "Explication pour Option1"
                                    }},
                                    {{
                                        "id": "b",
                                        "text": "Option2",
                                        "explanation": "Explication pour Option2"
                                    }}
                                ],
                                "answer": "a",
                                "explanation": "Explication détaillée de la réponse correcte"
                            }},
                            {{
                                "id": "q2",
                                "question": "Question?",
                                "options": [
                                    {{
                                        "id": "a",
                                        "text": "Option1",
                                        "explanation": "Explication pour Option1"
                                    }},
                                    {{
                                        "id": "b",
                                        "text": "Option2",
                                        "explanation": "Explication pour Option2"
                                    }}
                                ],
                                "answer": "a",
                                "explanation": "Explication détaillée de la réponse correcte"
                            }}
                        ]
                    }}
                ]
            }}
            // Répéter pour les autres chapitres
        ],
        "cover": "cover-image.png",
        "presentation_video": {{
            "url": "https://youtu.be/video-id",
            "type": "video",
            "description": "description_video",
            "transcript": "transcription_video"
        }},
        "resources": [
            {{
                "id": "resource-1",
                "title": "titre_ressource",
                "type": "type_ressource",
                "url": "url_ressource",
                "description": "description_ressource"
            }}
        ],
        "certification": {{
            "available": true,
            "title": "titre_certification",
            "description": "description_certification",
            "requirements": [
                "exigence1",
                "exigence2"
            ]
        }}
    }}
}}

EXIGENCES DE QUALITÉ:
1. Contenu adapté au niveau {inputs['level']}
2. Contenu en {inputs['language']}
3. Retourner uniquement le JSON, sans texte avant ou après
4. Chaque chapitre doit avoir:
   - Une description détaillée
   - Des objectifs d'apprentissage spécifiques
   - Au moins 2 contenus de type TEXT avec structure complète
   - Au moins 1 contenu de type VIDEO
   - Au moins 1 contenu de type AUDIO
   - Un exercice pratique
   - Un quiz avec 3-4 questions et explications
5. Générer au moins 4 chapitres selon la durée spécifiée
6. Inclure des ressources supplémentaires pertinentes
7. Adapter la difficulté du contenu et des exercices au niveau spécifié

RETOURNER UNIQUEMENT LE JSON GÉNÉRÉ, SANS TEXTE AVANT OU APRÈS"""


def generate_chapter_content_prompt(chapter_info: Dict, course_info: Dict = None) -> str:
    """
    Génère un prompt pour créer le contenu détaillé d'un chapitre spécifique.
    
    Args:
        chapter_info: Informations sur le chapitre (titre, description, etc.)
        course_info: Informations générales sur le cours (optionnel)
        
    Returns:
        Un prompt optimisé pour l'API Gemini
    """
    context = ""
    level = "INTERMEDIATE"
    language = "French"
    subject = ""
    
    if course_info:
        context = course_info.get('context', '')
        level = course_info.get('level', 'INTERMEDIATE')
        language = course_info.get('language', 'French')
        subject = course_info.get('subject', '')
    
    return f"""
En tant qu'expert pédagogique, développe le contenu détaillé du chapitre suivant:

CONTEXTE DU CHAPITRE:
- Titre: {chapter_info.get('title', 'Chapitre sans titre')}
- Description: {chapter_info.get('description', 'Aucune description fournie')}
{f"- Sujet global du cours: {subject}" if subject else ""}
{f"- Niveau: {level}" if level else ""}
{f"- Public cible: {context}" if context else ""}

TÂCHE:
Crée un contenu pédagogique structuré pour ce chapitre qui respecte EXACTEMENT ce format JSON:
{{
    "id": "{chapter_info.get('id', 'chapter-new')}",
    "title": "{chapter_info.get('title', 'Chapitre sans titre')}",
    "order": {chapter_info.get('order', 1)},
    "duration": "{chapter_info.get('duration', '00:45:00')}",
    "xp": {chapter_info.get('xp', 10)},
    "description": "{chapter_info.get('description', 'Description du chapitre')}",
    "contents": [
        {{
            "id": "{chapter_info.get('id', 'chapter-new')}-content-1",
            "title": "Titre de la première section",
            "lesson": "<p>Contenu HTML détaillé avec explications, exemples et mise en forme.</p><p>Plusieurs paragraphes avec contenu substantiel.</p>",
            "order": 1,
            "type": "TEXT",
            "duration": "00:15:00",
            "chapter_id": "{chapter_info.get('id', 'chapter-new')}",
            "title_chapter": "{chapter_info.get('title', 'Chapitre sans titre')}",
            "media_type": "TEXT",
            "media": null
        }},
        {{
            "id": "{chapter_info.get('id', 'chapter-new')}-content-2",
            "title": "Titre de la deuxième section",
            "lesson": "<p>Contenu HTML détaillé pour la deuxième section.</p>",
            "order": 2,
            "type": "TEXT",
            "duration": "00:10:00",
            "chapter_id": "{chapter_info.get('id', 'chapter-new')}",
            "title_chapter": "{chapter_info.get('title', 'Chapitre sans titre')}",
            "media_type": "TEXT",
            "media": null
        }},
        {{
            "id": "{chapter_info.get('id', 'chapter-new')}-video-1",
            "title": "Vidéo explicative sur le sujet",
            "lesson": "<p>Description du contenu de la vidéo et points clés abordés.</p>",
            "order": 3,
            "type": "VIDEO",
            "duration": "00:08:00",
            "chapter_id": "{chapter_info.get('id', 'chapter-new')}",
            "title_chapter": "{chapter_info.get('title', 'Chapitre sans titre')}",
            "media_type": "VIDEO",
            "media": {{
                "url": "https://example.com/video-url",
                "thumbnail": "https://example.com/thumbnail.jpg",
                "transcript": "Transcription complète du contenu de la vidéo..."
            }}
        }},
        {{
            "id": "{chapter_info.get('id', 'chapter-new')}-audio-1",
            "title": "Synthèse audio des points clés",
            "lesson": "<p>Description du contenu audio et comment l'utiliser efficacement.</p>",
            "order": 4,
            "type": "AUDIO",
            "duration": "00:05:00",
            "chapter_id": "{chapter_info.get('id', 'chapter-new')}",
            "title_chapter": "{chapter_info.get('title', 'Chapitre sans titre')}",
            "media_type": "AUDIO",
            "media": {{
                "url": "https://example.com/audio-url",
                "transcript": "Transcription complète du contenu audio..."
            }}
        }},
        {{
            "id": "{chapter_info.get('id', 'chapter-new')}-exercise-1",
            "title": "Exercice pratique",
            "order": 5,
            "type": "EXERCISE",
            "duration": "00:20:00",
            "chapter_id": "{chapter_info.get('id', 'chapter-new')}",
            "title_chapter": "{chapter_info.get('title', 'Chapitre sans titre')}",
            "content": {{
                "description": "Description détaillée de l'exercice à réaliser",
                "steps": [
                    "Étape 1: Instructions précises",
                    "Étape 2: Instructions précises",
                    "Étape 3: Instructions précises"
                ],
                "expected_output": "Description du résultat attendu",
                "hints": [
                    "Indice 1 pour aider l'apprenant",
                    "Indice 2 pour aider l'apprenant"
                ],
                "solution": "Solution détaillée de l'exercice"
            }}
        }}
    ]
}}

EXIGENCES DE QUALITÉ:
1. Contenu pédagogique de haute qualité adapté au niveau {level}
2. Contenu entièrement en {language}
3. Sections de TEXT avec HTML bien formaté (paragraphes, listes, mise en valeur)
4. Vidéo et audio avec descriptions pertinentes et transcriptions
5. Exercice pratique concret avec étapes claires et solution
6. Durées réalistes pour chaque type de contenu
7. Progression logique entre les sections

RETOURNER UNIQUEMENT LE JSON GÉNÉRÉ, SANS TEXTE AVANT OU APRÈS
"""

def generate_quiz_prompt(chapter_info: Dict, course_info: Dict = None) -> str:
    """
    Génère un prompt pour créer un quiz détaillé pour un chapitre spécifique.
    
    Args:
        chapter_info: Informations sur le chapitre
        course_info: Informations générales sur le cours (optionnel)
        
    Returns:
        Un prompt optimisé pour l'API Gemini
    """
    context = ""
    level = "INTERMEDIATE"
    language = "French"
    
    if course_info:
        context = course_info.get('context', '')
        level = course_info.get('level', 'INTERMEDIATE')
        language = course_info.get('language', 'French')
    
    chapter_title = chapter_info.get('title', 'Chapitre sans titre')
    chapter_description = chapter_info.get('description', '')
    
    return f"""
En tant qu'expert pédagogique, crée un quiz complet et pertinent pour le chapitre suivant:

CONTEXTE:
- Titre du chapitre: {chapter_title}
- Description du chapitre: {chapter_description}
{f"- Niveau: {level}" if level else ""}
{f"- Public cible: {context}" if context else ""}

TÂCHE:
Crée un quiz qui évalue efficacement la compréhension des concepts clés du chapitre.
Le quiz doit suivre EXACTEMENT ce format JSON:

{{
    "id": "{chapter_info.get('id', 'chapter-new')}-quiz",
    "title": "Quiz: {chapter_title}",
    "order": 99,
    "type": "QUIZ",
    "duration": "00:10:00",
    "chapter_id": "{chapter_info.get('id', 'chapter-new')}",
    "title_chapter": "{chapter_title}",
    "questions": [
        {{
            "id": "q1",
            "question": "Question 1 sur le contenu du chapitre?",
            "options": [
                {{
                    "id": "a",
                    "text": "Option 1 (réponse correcte)",
                    "explanation": "Explication brève pour cette option"
                }},
                {{
                    "id": "b",
                    "text": "Option 2",
                    "explanation": "Explication brève pour cette option"
                }},
                {{
                    "id": "c",
                    "text": "Option 3",
                    "explanation": "Explication brève pour cette option"
                }},
                {{
                    "id": "d",
                    "text": "Option 4",
                    "explanation": "Explication brève pour cette option"
                }}
            ],
            "answer": "a",
            "explanation": "Explication détaillée de la réponse correcte"
        }},
        {{
            "id": "q2",
            "question": "Question 2 sur le contenu du chapitre?",
            "options": [
                {{
                    "id": "a",
                    "text": "Option 1",
                    "explanation": "Explication brève pour cette option"
                }},
                {{
                    "id": "b",
                    "text": "Option 2 (réponse correcte)",
                    "explanation": "Explication brève pour cette option"
                }},
                {{
                    "id": "c",
                    "text": "Option 3",
                    "explanation": "Explication brève pour cette option"
                }},
                {{
                    "id": "d",
                    "text": "Option 4",
                    "explanation": "Explication brève pour cette option"
                }}
            ],
            "answer": "b",
            "explanation": "Explication détaillée de la réponse correcte"
        }},
        {{
            "id": "q3",
            "question": "Question 3 sur le contenu du chapitre?",
            "options": [
                {{
                    "id": "a",
                    "text": "Option 1",
                    "explanation": "Explication brève pour cette option"
                }},
                {{
                    "id": "b",
                    "text": "Option 2",
                    "explanation": "Explication brève pour cette option"
                }},
                {{
                    "id": "c",
                    "text": "Option 3 (réponse correcte)",
                    "explanation": "Explication brève pour cette option"
                }},
                {{
                    "id": "d",
                    "text": "Option 4",
                    "explanation": "Explication brève pour cette option"
                }}
            ],
            "answer": "c",
            "explanation": "Explication détaillée de la réponse correcte"
        }},
        {{
            "id": "q4",
            "question": "Question 4 sur le contenu du chapitre?",
            "options": [
                {{
                    "id": "a",
                    "text": "Option 1",
                    "explanation": "Explication brève pour cette option"
                }},
                {{
                    "id": "b",
                    "text": "Option 2",
                    "explanation": "Explication brève pour cette option"
                }},
                {{
                    "id": "c",
                    "text": "Option 3",
                    "explanation": "Explication brève pour cette option"
                }},
                {{
                    "id": "d",
                    "text": "Option 4 (réponse correcte)",
                    "explanation": "Explication brève pour cette option"
                }}
            ],
            "answer": "d",
            "explanation": "Explication détaillée de la réponse correcte"
        }}
    ]
}}

EXIGENCES DE QUALITÉ:
1. Créer EXACTEMENT 4 questions à choix multiples
2. Chaque question doit tester un concept clé différent du chapitre
3. Chaque question doit avoir EXACTEMENT 4 options de réponse
4. Les questions doivent être de difficulté adaptée au niveau {level}
5. Les explications doivent être précises et pédagogiques
6. Le contenu doit être intégralement en {language}
7. Éviter les questions ambiguës ou sujettes à interprétation
8. Assurer une variété dans les types de questions (concept, application, analyse)

RETOURNER UNIQUEMENT LE JSON GÉNÉRÉ, SANS TEXTE AVANT OU APRÈS
"""

def generate_exercise_prompt(chapter_info: Dict, course_info: Dict = None) -> str:
    """
    Génère un prompt pour créer un exercice pratique pour un chapitre spécifique.
    
    Args:
        chapter_info: Informations sur le chapitre
        course_info: Informations générales sur le cours (optionnel)
        
    Returns:
        Un prompt optimisé pour l'API Gemini
    """
    context = ""
    level = "INTERMEDIATE"
    language = "French"
    subject = ""
    
    if course_info:
        context = course_info.get('context', '')
        level = course_info.get('level', 'INTERMEDIATE')
        language = course_info.get('language', 'French')
        subject = course_info.get('subject', '')
    
    chapter_title = chapter_info.get('title', 'Chapitre sans titre')
    chapter_description = chapter_info.get('description', '')
    
    return f"""
En tant qu'expert pédagogique, crée un exercice pratique pertinent pour le chapitre suivant:

CONTEXTE:
- Titre du chapitre: {chapter_title}
- Description du chapitre: {chapter_description}
{f"- Sujet global du cours: {subject}" if subject else ""}
{f"- Niveau: {level}" if level else ""}
{f"- Public cible: {context}" if context else ""}

TÂCHE:
Crée un exercice pratique et engageant qui permet d'appliquer les concepts clés du chapitre.
L'exercice doit suivre EXACTEMENT ce format JSON:

{{
    "id": "{chapter_info.get('id', 'chapter-new')}-exercise",
    "title": "Exercice pratique: {chapter_title}",
    "order": 98,
    "type": "EXERCISE",
    "duration": "00:30:00",
    "chapter_id": "{chapter_info.get('id', 'chapter-new')}",
    "title_chapter": "{chapter_title}",
    "content": {{
        "description": "Description détaillée et contextualisée de l'exercice à réaliser",
        "objectives": [
            "Objectif pédagogique 1 de l'exercice",
            "Objectif pédagogique 2 de l'exercice",
            "Objectif pédagogique 3 de l'exercice"
        ],
        "prerequisites": [
            "Prérequis 1 nécessaire pour réaliser l'exercice",
            "Prérequis 2 nécessaire pour réaliser l'exercice"
        ],
        "steps": [
            "Étape 1: Instructions détaillées pour cette étape",
            "Étape 2: Instructions détaillées pour cette étape",
            "Étape 3: Instructions détaillées pour cette étape",
            "Étape 4: Instructions détaillées pour cette étape"
        ],
        "resources": [
            "Ressource 1 utile pour l'exercice",
            "Ressource 2 utile pour l'exercice"
        ],
        "expected_output": "Description détaillée du résultat attendu à la fin de l'exercice",
        "hints": [
            "Indice 1 pour aider l'apprenant si nécessaire",
            "Indice 2 pour aider l'apprenant si nécessaire",
            "Indice 3 pour aider l'apprenant si nécessaire"
        ],
        "solution": "Solution complète et détaillée de l'exercice, expliquant chaque étape et justifiant les choix effectués"
    }}
}}

EXIGENCES DE QUALITÉ:
1. Exercice réaliste et applicable dans un contexte professionnel
2. Instructions claires et étape par étape
3. Difficulté adaptée au niveau {level}
4. Contenu intégralement en {language}
5. Durée estimée réaliste (30 minutes par défaut)
6. Solution détaillée et éducative
7. Liens avec les concepts abordés dans le chapitre
8. Indications de progression et critères de réussite clairs

RETOURNER UNIQUEMENT LE JSON GÉNÉRÉ, SANS TEXTE AVANT OU APRÈS
"""

def generate_resource_prompt(course_info: Dict) -> str:
    """
    Génère un prompt pour créer des ressources complémentaires pour un cours.
    
    Args:
        course_info: Informations générales sur le cours
        
    Returns:
        Un prompt optimisé pour l'API Gemini
    """
    subject = course_info.get('subject', '')
    level = course_info.get('level', 'INTERMEDIATE')
    language = course_info.get('language', 'French')
    
    return f"""
En tant qu'expert pédagogique, crée une liste de ressources complémentaires pour le cours suivant:

CONTEXTE:
- Sujet du cours: {subject}
- Niveau: {level}
- Langue: {language}

TÂCHE:
Crée une liste de ressources pédagogiques pertinentes qui enrichiront le cours.
Les ressources doivent suivre EXACTEMENT ce format JSON:

{{
    "resources": [
        {{
            "id": "resource-1",
            "title": "Titre de la ressource 1",
            "type": "article/video/ebook/tool/website",
            "url": "https://example.com/ressource1",
            "description": "Description détaillée de la ressource et de sa pertinence pour le cours",
            "language": "Langue de la ressource",
            "difficulty": "Niveau de difficulté (débutant/intermédiaire/avancé)",
            "estimated_time": "Temps estimé pour consulter cette ressource (ex: 30 min)"
        }},
        {{
            "id": "resource-2",
            "title": "Titre de la ressource 2",
            "type": "article/video/ebook/tool/website",
            "url": "https://example.com/ressource2",
            "description": "Description détaillée de la ressource et de sa pertinence pour le cours",
            "language": "Langue de la ressource",
            "difficulty": "Niveau de difficulté (débutant/intermédiaire/avancé)",
            "estimated_time": "Temps estimé pour consulter cette ressource (ex: 1h)"
        }},
        // 6 à 8 ressources au total
    ]
}}

EXIGENCES DE QUALITÉ:
1. Fournir 6 à 8 ressources diversifiées (articles, vidéos, livres, outils, sites web)
2. Ressources pertinentes et spécifiques au sujet du cours
3. Ressources principalement en {language}, avec quelques exceptions possibles en anglais si pertinent
4. Ressources adaptées au niveau {level}
5. Descriptions détaillées et informatives
6. URLs réalistes (peuvent être fictives mais crédibles)
7. Varier les types de ressources et les sources
8. Indiquer si possible des ressources gratuites et payantes

RETOURNER UNIQUEMENT LE JSON GÉNÉRÉ, SANS TEXTE AVANT OU APRÈS
"""

def generate_video_transcript_prompt(video_info: Dict, course_info: Dict = None) -> str:
    """
    Génère un prompt pour créer une transcription de vidéo pédagogique.
    
    Args:
        video_info: Informations sur la vidéo
        course_info: Informations générales sur le cours (optionnel)
        
    Returns:
        Un prompt optimisé pour l'API Gemini
    """
    title = video_info.get('title', 'Vidéo sans titre')
    description = video_info.get('description', '')
    duration = video_info.get('duration', '00:10:00')
    
    level = "INTERMEDIATE"
    language = "French"
    subject = ""
    
    if course_info:
        level = course_info.get('level', 'INTERMEDIATE')
        language = course_info.get('language', 'French')
        subject = course_info.get('subject', '')
    
    return f"""
En tant qu'expert pédagogique, crée une transcription réaliste pour une vidéo éducative avec les caractéristiques suivantes:

CONTEXTE:
- Titre de la vidéo: {title}
- Description: {description}
- Durée: {duration}
{f"- Sujet global du cours: {subject}" if subject else ""}
{f"- Niveau: {level}" if level else ""}

TÂCHE:
Crée une transcription complète et détaillée telle qu'elle serait prononcée par un formateur professionnel.
La transcription doit suivre EXACTEMENT ce format JSON:

{{
    "transcript": {{
        "title": "{title}",
        "duration": "{duration}",
        "speaker": "Nom du formateur",
        "content": "Transcription complète du texte tel qu'il serait prononcé, avec introduction, développement et conclusion. Le texte doit être naturel, inclure des salutations, transitions, et une conclusion."
    }}
}}

EXIGENCES DE QUALITÉ:
1. Texte naturel comme parlé dans une vidéo pédagogique professionnelle
2. Contenu entièrement en {language}
3. Ton conversationnel mais expert
4. Inclusion d'éléments didactiques:
   - Introduction claire ("Bonjour et bienvenue à cette vidéo sur...")
   - Structure logique et transitions
   - Références à ce que le spectateur voit ("Comme vous pouvez le voir à l'écran...")
   - Questions rhétoriques pour maintenir l'engagement
   - Conclusion et appel à l'action
5. Niveau de langage adapté au public {level}
6. Longueur cohérente avec la durée indiquée ({duration})

RETOURNER UNIQUEMENT LE JSON GÉNÉRÉ, SANS TEXTE AVANT OU APRÈS
"""

def generate_certification_prompt(course_info: Dict) -> str:
    """
    Génère un prompt pour créer une structure de certification pour un cours.
    
    Args:
        course_info: Informations générales sur le cours
        
    Returns:
        Un prompt optimisé pour l'API Gemini
    """
    subject = course_info.get('subject', '')
    level = course_info.get('level', 'INTERMEDIATE')
    language = course_info.get('language', 'French')
    
    return f"""
En tant qu'expert pédagogique, crée une structure de certification professionnelle pour le cours suivant:

CONTEXTE:
- Sujet du cours: {subject}
- Niveau: {level}
- Langue: {language}

TÂCHE:
Crée une structure de certification complète qui valide les compétences acquises dans ce cours.
La certification doit suivre EXACTEMENT ce format JSON:

{{
    "certification": {{
        "title": "Certification professionnelle: {subject}",
        "available": true,
        "description": "Description détaillée de cette certification et de sa valeur pour les apprenants",
        "duration": "02:00:00",
        "passing_score": 80,
        "requirements": [
            "Exigence 1 pour obtenir la certification",
            "Exigence 2 pour obtenir la certification",
            "Exigence 3 pour obtenir la certification"
        ],
        "skills_validated": [
            "Compétence 1 validée par cette certification",
            "Compétence 2 validée par cette certification",
            "Compétence 3 validée par cette certification",
            "Compétence 4 validée par cette certification"
        ],
        "exam_format": {{
            "total_questions": 40,
            "question_types": [
                "QCM (60%)",
                "Questions ouvertes (20%)",
                "Études de cas (20%)"
            ],
            "time_limit": "120 minutes",
            "attempts_allowed": 2
        }},
        "preparation_tips": [
            "Conseil 1 pour réussir l'examen",
            "Conseil 2 pour réussir l'examen",
            "Conseil 3 pour réussir l'examen"
        ],
        "industry_recognition": "Description de la reconnaissance de cette certification dans l'industrie"
    }}
}}

EXIGENCES DE QUALITÉ:
1. Certification réaliste et professionnelle
2. Contenu entièrement en {language}
3. Niveau adapté à la complexité du sujet et au niveau {level}
4. Exigences claires et mesurables
5. Format d'examen cohérent avec les bonnes pratiques du secteur
6. Compétences validées spécifiques et pertinentes
7. Description qui met en valeur l'utilité de la certification

RETOURNER UNIQUEMENT LE JSON GÉNÉRÉ, SANS TEXTE AVANT OU APRÈS
"""
# </invoke>