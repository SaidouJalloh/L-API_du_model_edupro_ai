import requests

url = "http://127.0.0.1:5000/generate_course"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer ImamSaid95"
}
data = {
    "subject": "Python",
    "format_type": "vidéo",
    "level": "débutant",
    "duration": 5,
    "duration_unit": "heures",
    "language": "français",
    "context": "formation en ligne"
}

response = requests.post(url, json=data, headers=headers)
print(response.json())  # Affiche la réponse de l'API
