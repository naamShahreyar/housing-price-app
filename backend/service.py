import joblib
import numpy as np
import json
import os

from src.logger import get_logger
from src.constants.config import config

logger = get_logger(__name__)


class PredictionService:

    def __init__(self):
        self.model_path = config["artifacts"]["model_path"]
        self.feature_path = os.path.join(
            os.path.dirname(self.model_path),
            "features.json"
        )

        self.model = self._load_model()
        self.features = self._load_features()

    def _load_model(self):
        try:
            logger.info("Loading model...")
            model = joblib.load(self.model_path)
            logger.info("Model loaded successfully")
            return model
        except Exception as e:
            logger.exception(f"Failed to load model: {e}")
            raise e

    def _load_features(self):
        try:
            logger.info("Loading feature names...")
            with open(self.feature_path, "r") as f:
                features = json.load(f)
            logger.info("Feature names loaded")
            return features
        except Exception as e:
            logger.exception(f"Failed to load features: {e}")
            raise e

    def predict(self, data):
        try:
            logger.info("Running prediction")

            input_dict = data.dict()

            # Maintain training order
            ordered_features = [input_dict[f] for f in self.features]

            X = np.array(ordered_features).reshape(1, -1)

            prediction = self.model.predict(X)[0]

            return float(prediction)

        except Exception as e:
            logger.exception(f"Prediction failed: {e}")
            raise e