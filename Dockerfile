# Utiliser l'image de base Python
FROM python:3.10.6-buster

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires dans le répertoire /app du conteneur
COPY main.py model.joblib Pipfile Pipfile.lock /app/
COPY tests /app/tests

# Installer pipenv et les dépendances à partir du Pipfile
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

# Installer pytest pour exécuter les tests
RUN pipenv install pytest

# Ajouter PYTHONPATH pour que Python puisse trouver le module
ENV PYTHONPATH=/app

# Exécuter les tests avant le déploiement
RUN python -m pytest tests/

# Exposer le port 8000 pour FastAPI
EXPOSE 8000

# Commande pour lancer l'application FastAPI en utilisant Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
