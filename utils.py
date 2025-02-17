# def convert_duration_to_hours(duration, unit):
#     """Convertit la durée en heures selon l'unité choisie"""
#     conversions = {
#         "heures": 1,
#         "jours": 24,
#         "semaines": 24 * 7,
#         "mois": 24 * 30
#     }
#     return duration * conversions.get(unit, 1)  # Par défaut, garde la même durée

# def convert_duration_to_hours(duration, unit):
#     """Convertit une durée en heures en fonction de l'unité donnée."""
#     if unit == "minutes":
#         return duration / 60
#     elif unit == "jours":
#         return duration * 24
#     elif unit == "semaines":
#         return duration * 24 * 7
#     elif unit == "mois":
#         return duration * 24 * 30
#     else:
#         return duration

# def generate_course_prompt(inputs):
#     """Génère le prompt pour l'API Gemini"""
#     duration_hours = convert_duration_to_hours(inputs['duration'], inputs['duration_unit'])

#     return f"""En tant qu'expert en formation, génère un programme de formation avec la structure JSON suivante.

# Input:
# - Sujet: {inputs['subject']}
# - Format: {inputs['format_type']}
# - Niveau: {inputs['level']}
# - Durée: {duration_hours} heures
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




# # Derniere version avec le format adapter
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
#     """Génère le prompt pour l'API avec une structure JSON enrichie et un contenu détaillé"""
#     duration_hours = convert_duration_to_hours(inputs['duration'], inputs['duration_unit'])

#     return f"""
# En tant qu'expert en formation, génère un programme de formation avec la structure JSON suivante.

# Input:
# - Sujet: {inputs['subject']}
# - Format: {inputs['format_type']}
# - Niveau: {inputs['level']}
# - Durée: {duration_hours} heures
# - Langue: {inputs['language']}
# - Contexte: {inputs['context']}
# {f"- Prérequis: {inputs['prerequisites']}" if inputs.get('prerequisites') else ''}

# Format JSON à respecter:
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

# IMPORTANT:
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
# 7. Adapter la difficulté du contenu et des exercices au niveau spécifié"""



# Derniere version avec le format adapter
def convert_duration_to_hours(duration, unit):
    """Convertit la durée en heures selon l'unité choisie"""
    conversions = {
        "heures": 1,
        "jours": 24,
        "semaines": 24 * 7,
        "mois": 24 * 30
    }
    return duration * conversions.get(unit, 1)
def generate_course_prompt(inputs):
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
            }},
            {{
                "id": "chapter-2",
                "title": "titre_chapitre",
                "order": 2,
                "duration": "00:00:00",
                "xp": 10,
                "quiz_id": "quiz-2",
                "description": "description_chapitre",
                "contents": [
                    {{
                        "id": "content-3",
                        "title": "titre_contenu",
                        "lesson": "<p>introduction_section</p>",
                        "order": 1,
                        "type": "TEXT",
                        "duration": "00:00:00",
                        "chapter_id": "chapter-2",
                        "title_chapter": "titre_chapitre",
                        "media_type": "TEXT",
                        "media": null
                    }},
                    {{
                        "id": "content-4",
                        "title": "titre_contenu",
                        "lesson": "<p>introduction_section</p>",
                        "order": 2,
                        "type": "TEXT",
                        "duration": "00:00:00",
                        "chapter_id": "chapter-2",
                        "title_chapter": "titre_chapitre",
                        "media_type": "TEXT",
                        "media": null
                    }},
                    {{
                        "id": "exercise-2",
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
                        "id": "quiz-2",
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
            }},
            {{
                "id": "chapter-3",
                "title": "titre_chapitre",
                "order": 3,
                "duration": "00:00:00",
                "xp": 10,
                "quiz_id": "quiz-3",
                "description": "description_chapitre",
                "contents": [
                    {{
                        "id": "content-5",
                        "title": "titre_contenu",
                        "lesson": "<p>introduction_section</p>",
                        "order": 1,
                        "type": "TEXT",
                        "duration": "00:00:00",
                        "chapter_id": "chapter-3",
                        "title_chapter": "titre_chapitre",
                        "media_type": "TEXT",
                        "media": null
                    }},
                    {{
                        "id": "content-6",
                        "title": "titre_contenu",
                        "lesson": "<p>introduction_section</p>",
                        "order": 2,
                        "type": "TEXT",
                        "duration": "00:00:00",
                        "chapter_id": "chapter-3",
                        "title_chapter": "titre_chapitre",
                        "media_type": "TEXT",
                        "media": null
                    }},
                    {{
                        "id": "exercise-3",
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
                        "id": "quiz-3",
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
            }},
            {{
                "id": "chapter-4",
                "title": "titre_chapitre",
                "order": 4,
                "duration": "00:00:00",
                "xp": 10,
                "quiz_id": "quiz-4",
                "description": "description_chapitre",
                "contents": [
                    {{
                        "id": "content-7",
                        "title": "titre_contenu",
                        "lesson": "<p>introduction_section</p>",
                        "order": 1,
                        "type": "TEXT",
                        "duration": "00:00:00",
                        "chapter_id": "chapter-4",
                        "title_chapter": "titre_chapitre",
                        "media_type": "TEXT",
                        "media": null
                    }},
                    {{
                        "id": "content-8",
                        "title": "titre_contenu",
                        "lesson": "<p>introduction_section</p>",
                        "order": 2,
                        "type": "TEXT",
                        "duration": "00:00:00",
                        "chapter_id": "chapter-4",
                        "title_chapter": "titre_chapitre",
                        "media_type": "TEXT",
                        "media": null
                    }},
                    {{
                        "id": "exercise-4",
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
                        "id": "quiz-4",
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

le contenu que tu dois generer doit etre au format json,surtout j'insiste sur le fait que tu dois retourner uniquement le json sans texte avant ou apres
1. Contenu adapté au niveau {inputs['level']}
2. Contenu en {inputs['language']}
3. Retourner uniquement le JSON, sans texte avant ou après
4. Chaque chapitre doit avoir:
   - Une description détaillée
   - Des objectifs d'apprentissage spécifiques
   - Au moins 2 contenus de type TEXT avec structure complète
   -au moins 1 contenus de type video
   -au moins 1 contenus de type audio
   - Un exercice pratique
   - Un quiz avec 3-4 questions et explications
5. Générer au moins 4 chapitres selon la durée spécifiée
6. Inclure des ressources supplémentaires pertinentes
7. Adapter la difficulté du contenu et des exercices au niveau spécifié
EXIGENCES DE QUALITÉ:
1. Contenu:
   - Précision technique et factuelle
   - Sources et références vérifiables
   - Exemples concrets et actualisés
   - Terminologie professionnelle adaptée

2. Pédagogie:
   - Instructions claires et détaillées
   - Progression logique des apprentissages
   - Interactivité et engagement
   - Évaluation continue des acquis

3. Format:
   - Structure JSON valide et complète
   - Durées adaptées au format et niveau
   - Médias variés et pertinents
   - Ressources téléchargeables utiles

4. Validation:
   - Critères de réussite explicites
   - Tests de connaissances réguliers
   - Exercices pratiques notés
   - Certification avec prérequis clairs

RETOURNER UNIQUEMENT LE JSON GÉNÉRÉ, SANS TEXTE AVANT OU APRÈS"""