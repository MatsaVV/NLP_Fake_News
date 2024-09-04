# Use Python base image from Docker Hub
FROM python:3.10.6-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy necessary files to the /app folder in the container
COPY main.py /app/main.py
COPY model.joblib /app/model.joblib
COPY Pipfile /app/Pipfile
COPY Pipfile.lock /app/Pipfile.lock

# Install pipenv and dependencies from the Pipfile
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

# Expose the port stremlit en plus
EXPOSE 8000

# Command to run the FastAPI application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
