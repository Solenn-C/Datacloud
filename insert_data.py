import requests
from dotenv import load_dotenv
from pymongo import MongoClient, errors
import os, dotenv

# Charger les variables d'environnement du fichier .env
load_dotenv()

# Lire la variable d'environnement
uri = os.getenv("URI_MONGODB")

if not uri:
    raise ValueError("⚠️  URI_MONGODB n'est pas défini dans le fichier .env")

# Connexion à MongoDB
client = MongoClient(uri)
db = client["Data_paris"]
collection = db["velib"]

# Création d'un index unique sur stationcode (avant toute insertion)
collection.create_index("stationcode", unique=True)

# Récupération des données depuis l'API Vélib
response = requests.get(
    "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/records?limit=100"
)
data = response.json()

# Vérifie qu'il y a bien une clé "results"
if "results" in data:
    documents = data["results"]

    if documents:
        try:
            # Insertion dans MongoDB
            collection.insert_many(documents, ordered=False)
            print(f"{len(documents)} stations Vélib insérées avec succès 🚴‍♂️")
        except errors.BulkWriteError as e:
            print("Certaines stations existent déjà, insertion partielle effectuée ✅")
    else:
        print("Aucune donnée à insérer.")
else:
    print("Structure de réponse inattendue :", data.keys())