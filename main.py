import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from joblib import load
import joblib
import os

class TextItem(BaseModel):
    title: str
    text: str
    subject: str
    date: str

app = FastAPI()
model = joblib.load("model.joblib")

# Fonction pour préparer les données d'entrée sous forme de DataFrame
def create_input_dataframe(item: TextItem) -> pd.DataFrame:
    return pd.DataFrame([{
        'title': item.title,
        'text': item.text,
        'subject': item.subject,
        'date': item.date
    }])

# Créer un endpoint pour faire des prédictions
@app.post("/predict/")
async def predict(item: TextItem):
    try:
        # Créer un DataFrame à partir des données entrantes
        input_data = create_input_dataframe(item)

        # Faire la prédiction
        prediction = model.predict(input_data)[0].lower()  # Utiliser lower() si nécessaire

        # Retourner la prédiction complète
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Route pour vérifier que l'API est en ligne
@app.get("/")
async def root():
    return {"message": "API de détection de Fake News en fonctionnement!"}
