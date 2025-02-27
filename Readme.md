Guide de test des endpoints pour l'API de Génération de Cours
URL de base
http://localhost:8282
1. Vérification de l'état de l'API
Endpoint: /health
Type: GET
Body: Aucun
2. Génération de cours
Endpoint: /generate-course
Type: POST
Body:
jsonCopy{
    "subject": "Intelligence Artificielle",
    "format_type": "online",
    "level": "intermediate",
    "duration": 4,
    "duration_unit": "hours",
    "language": "français",
    "context": "Ce cours est destiné à des ingénieurs avec une expérience en programmation"
}
Paramètres URL optionnels:

mode=structure - génère uniquement la structure
mode=complete - génère le cours complet (par défaut)
mode=progressive - génère la structure puis enrichit progressivement

3. Génération d'un chapitre
Endpoint: /generate-chapter
Type: POST
Body:
jsonCopy{
    "chapter_info": {
        "title": "Apprentissage par renforcement",
        "level": "intermediate",
        "duration": 45,
        "duration_unit": "minutes"
    },
    "course_info": {
        "subject": "Intelligence Artificielle",
        "level": "intermediate",
        "language": "français",
        "context": "Pour des ingénieurs avec une expérience en programmation"
    },
    "include_quiz": true,
    "include_exercise": true
}
4. Génération d'un quiz
Endpoint: /generate-quiz
Type: POST
Body:
jsonCopy{
    "chapter_info": {
        "title": "Réseaux de neurones convolutifs",
        "level": "intermediate"
    },
    "course_info": {
        "subject": "Deep Learning",
        "level": "intermediate",
        "language": "français"
    }
}
5. Génération d'un exercice
Endpoint: /generate-exercise
Type: POST
Body:
jsonCopy{
    "chapter_info": {
        "title": "Réseaux de neurones convolutifs",
        "level": "intermediate"
    },
    "course_info": {
        "subject": "Deep Learning",
        "level": "intermediate",
        "language": "français"
    }
}
6. Génération de ressources
Endpoint: /generate-resources
Type: POST
Body:
jsonCopy{
    "course_info": {
        "subject": "Intelligence Artificielle",
        "level": "intermediate",
        "language": "français",
        "context": "Pour des ingénieurs avec une expérience en programmation Python",
        "chapters": ["Introduction à l'IA", "Apprentissage supervisé", "Réseaux de neurones"]
    }
}
7. Génération de transcription vidéo
Endpoint: /generate-video-transcript
Type: POST
Body:
jsonCopy{
    "video_info": {
        "title": "Introduction aux architectures CNN",
        "duration": 15,
        "duration_unit": "minutes",
        "level": "intermediate"
    },
    "course_info": {
        "subject": "Deep Learning",
        "level": "intermediate",
        "language": "français"
    }
}
8. Génération de certification
Endpoint: /generate-certification
Type: POST
Body:
jsonCopy{
    "course_info": {
        "id": "course-123",
        "title": "Formation complète en Intelligence Artificielle",
        "level": "intermediate",
        "language": "français",
        "duration": 20,
        "duration_unit": "hours"
    }
}
9. Mise à jour d'un chapitre
Endpoint: /update-chapter
Type: PUT
Body:
jsonCopy{
    "chapter_id": "chapter-123",
    "course_id": "course-456",
    "updates": {
        "title": "Nouveau titre du chapitre",
        "duration": 45,
        "level": "advanced"
    }
}
10. Ajout de contenu à un chapitre
Endpoint: /add-content-to-chapter
Type: POST
Body:
jsonCopy{
    "chapter_id": "chapter-123",
    "content_type": "QUIZ",
    "chapter_info": {
        "id": "chapter-123",
        "title": "Introduction aux réseaux de neurones",
        "level": "intermediate"
    },
    "course_info": {
        "subject": "Intelligence Artificielle",
        "level": "intermediate",
        "language": "français"
    }
}
Valeurs possibles pour content_type: "TEXT", "VIDEO", "AUDIO", "EXERCISE", "QUIZ"
11. Statistiques du cache
Endpoint: /cache-stats
Type: GET
Body: Aucun
Si vous voulez générer uniquement la structure du cours (comme une table des matières, sans le contenu détaillé):
Copyhttp://localhost:8282/generate-course?mode=structure

Si vous voulez générer le cours complet avec tout son contenu (c'est l'option par défaut si vous ne spécifiez pas de mode):
Copyhttp://localhost:8282/generate-course?mode=complete
ou simplement:
Copyhttp://localhost:8282/generate-course

Si vous voulez utiliser le mode progressif (qui génère d'abord la structure puis enrichit progressivement le contenu):
Copyhttp://localhost:8282/generate-course?mode=progressive


Dans Postman, vous ajouteriez ces paramètres dans la section "Params" de l'onglet de requête, ou directement dans l'URL comme montré ci-dessus.
Le corps (body) de la requête reste le même dans tous les cas, ce qui change c'est uniquement comment l'API va générer et retourner le contenu en fonction du paramètre mode que vous ajoutez à l'URL.