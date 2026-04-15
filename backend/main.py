from fastapi import FastAPI, HTTPException
from backend.schema import HouseInput, PredictionOutput
from backend.service import PredictionService

from src.logger import get_logger

logger = get_logger(__name__)

app = FastAPI(title="House Price Prediction API", version="1.0")

# Load once at startup
prediction_service = PredictionService()


@app.get("/")
def root():
    return {"message": "House Price Prediction API is running"}


@app.post("/predict", response_model=PredictionOutput)
def predict(data: HouseInput):
    try:
        prediction = prediction_service.predict(data)
        return {"prediction": prediction}

    except Exception as e:
        logger.exception(f"Error in /predict endpoint: {e}")
        raise HTTPException(status_code=500, detail="Prediction failed")