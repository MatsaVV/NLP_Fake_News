import joblib
import pytest

def test_model_loading():
    try:
        model = joblib.load("model.joblib")
        assert model is not None
    except Exception as e:
        pytest.fail(f"Le modèle n'a pas pu être chargé: {str(e)}")
