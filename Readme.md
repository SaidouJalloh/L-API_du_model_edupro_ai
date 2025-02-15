# Générateur de Plans de Cours API

API simple pour générer des plans de cours structurés en utilisant Gemini Pro.

## Installation

1. Cloner le repository :
```bash
git clone <votre-repo>
cd <votre-repo>
```

2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

3. Créer un fichier `.env` :
```
GEMINI_API_KEY=votre_clé_api
API_SECRET_KEY
PORT=8282
```

## Utilisation Locale

1. Lancer l'API :
```bash
python main.py
```

2. Tester l'API avec postman :
```bash
curl -X POST http://localhost:5000/generate-course \
-H "Content-Type: application/json" \
-H "X-API-Key: "Le password defini dans l'.env
Boby '{
    "subject": "Python pour débutants",
    "format_type": "en ligne",
    "level": "débutant",
    "duration": 10,
    "duration_unit": "heures",
    "language": "français",
    "context": "Formation développeurs web",
    "prerequisites": "Aucun"
}'
send enter
```

## Documentation

Accédez à la documentation de l'API via `/docs`

## Déploiement sur DigitalOcean

1. Créez un nouveau repository GitHub et poussez votre code

2. Sur DigitalOcean :
   - Allez dans "Apps" > "Create App"
   - Choisissez GitHub comme source
   - Sélectionnez votre repository
   - Configurez les variables d'environnement :
     - `GEMINI_API_KEY`
     - `PORT`
   - Déployez l'application

3. DigitalOcean va automatiquement déployer votre API et vous fournir une URL

## Structure des Fichiers

```
.
├── .env
├── .gitignore
├── app.py
    main.py
├── utils.py
├── requirements.txt
└── README.md
```

## Endpoints

- `GET /health` : Vérifie l'état de l'API
- `GET /docs` : Documentation de l'API
- `POST /generate-course` : Génère un plan de cours