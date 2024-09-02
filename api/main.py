from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
from typing import Dict

# Charger le modèle pré-entraîné
with open("api/model.pkl", "rb") as f:
    model = pickle.load(f)

# Initialiser l'application FastAPI
app = FastAPI()

# Classe pour représenter la requête
class Article(BaseModel):
    title: str
    content: str

# Endpoint pour prédire si un article est fake ou vrai
@app.post("/predict")
async def predict(article: Article):
    try:
        # Faire une prédiction
        prediction = model.predict([article.content])
        confidence = max(model.predict_proba([article.content])[0])
        return {"prediction": prediction[0], "confidence": f"{confidence * 100:.2f}%"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint de test
@app.get("/")
async def root():
    return {"message": "Fake News Detection API is running"}
