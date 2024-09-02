import requests
import json

def test_predict():
    url = 'http://localhost:8000/predict/'  # Adjust the URL based on your server configuration
    data = {"text": "Example news text that is clearly fake."}
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, data=json.dumps(data), headers=headers)
    response_data = response.json()

    assert response.status_code == 200
    assert 'prediction' in response_data  # Ensure there is a prediction key in the response
    assert response_data['prediction'] in ['Fake', 'True']  # Adjust based on your model's labels
