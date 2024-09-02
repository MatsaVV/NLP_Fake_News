import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from joblib import load
import os

# Définir la classe pour les données entrantes
class TextItem(BaseModel):
    title: str
    text: str
    subject: str
    date: str

app = FastAPI()

# Chemin vers le modèle pré-entraîné
MODEL_PATH = 'model.joblib'

# Charger le modèle de Naïve Bayes
if os.path.exists(MODEL_PATH):
    model = load(MODEL_PATH)
else:
    raise FileNotFoundError(f"Le modèle spécifié à '{MODEL_PATH}' n'a pas été trouvé.")

# Créer un endpoint pour faire des prédictions
@app.post("/predict/")
async def predict(item: TextItem):
    try:
        # Créer un DataFrame à partir des données entrantes
        input_data = pd.DataFrame([{
            'title': item.title,
            'text': item.text,
            'subject': item.subject,
            'date': item.date
        }])

        # Faire la prédiction
        prediction = model.predict(input_data)

        # Retourner la première prédiction
        return {"prediction": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Route pour vérifier que l'API est en ligne
@app.get("/")
async def root():
    return {"message": "API de détection de Fake News en fonctionnement!"}
