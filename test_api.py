# import requests

# url = "http://127.0.0.1:5000/generate_course"
# headers = {
#     "Content-Type": "application/json",
#     "Authorization": "Bearer ImamSaid95"
# }
# data = {
#     "subject": "Python",
#     "format_type": "vidéo",
#     "level": "débutant",
#     "duration": 5,
#     "duration_unit": "heures",
#     "language": "français",
#     "context": "formation en ligne"
# }

# response = requests.post(url, json=data, headers=headers)
# print(response.json())  # Affiche la réponse de l'API

import requests
import json
import os
from dotenv import load_dotenv

# Chargement des variables d'environnement
load_dotenv()

def test_api():
    base_url = "http://localhost:8282"
    api_key = os.getenv('API_SECRET_KEY')
    
    # Headers avec la clé API
    headers = {
        'Content-Type': 'application/json',
        'X-API-Key': api_key
    }
    
    # Données de test
    payload = {
        "subject": "Python pour débutants",
        "format_type": "en ligne",
        "level": "débutant",
        "duration": 10,
        "duration_unit": "heures",
        "language": "français",
        "context": "Formation pour développeurs web",
        "prerequisites": "Aucun"
    }

    # Test de la route /health
    print("\n=== Test Health Check ===")
    try:
        health_response = requests.get(f"{base_url}/health")
        print(f"Status Code: {health_response.status_code}")
        print(f"Response: {health_response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Health check failed: {str(e)}")
        return

    # Test de la documentation
    print("\n=== Test Documentation ===")
    try:
        docs_response = requests.get(f"{base_url}/docs")
        print(f"Status Code: {docs_response.status_code}")
        if docs_response.status_code == 200:
            print("Documentation accessible")
    except requests.exceptions.RequestException as e:
        print(f"Documentation check failed: {str(e)}")

    # Test de la génération de cours
    print("\n=== Test Course Generation ===")
    try:
        response = requests.post(
            f"{base_url}/generate-course",
            headers=headers,
            json=payload
        )
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            try:
                # Tentative de parser la réponse comme du JSON
                course_data = json.loads(response.text)
                print("\nGenerated Course Structure:")
                print(json.dumps(course_data, indent=2, ensure_ascii=False))
            except json.JSONDecodeError:
                # Si ce n'est pas du JSON, afficher le texte brut
                print("\nRaw Response:")
                print(response.text)
        else:
            try:
                error_data = response.json()
                print("\nError Response:")
                print(f"Error: {error_data.get('error', 'Unknown error')}")
                if 'details' in error_data:
                    print(f"Details: {error_data['details']}")
            except json.JSONDecodeError:
                print(f"\nRaw error response: {response.text}")
            
    except requests.exceptions.RequestException as e:
        print(f"\nRequest failed: {str(e)}")

def main():
    if not os.getenv('API_SECRET_KEY'):
        print("⚠️  Warning: API_SECRET_KEY not found in .env file")
        return
    
    print("🚀 Starting API Tests...")
    test_api()
    print("\n✅ Tests completed")

if __name__ == "__main__":
    main()