from src.constants.config import config
from src.logger import get_logger
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error
import pandas as pd
import joblib
import os

logger = get_logger(__name__)
class ModelTrainer:

    def __init__(self):
        self.model_path = config["artifacts"]["model_path"]
        self.n_estimators = config["model"]["n_estimators"]

    def run(self, processed_dir):
        
        try: 
            logger.info("Starting model training")

            X_train = pd.read_csv(f"{processed_dir}/X_train.csv")
            y_train = pd.read_csv(f"{processed_dir}/y_train.csv").values.ravel()

            X_test = pd.read_csv(f"{processed_dir}/X_test.csv")
            y_test = pd.read_csv(f"{processed_dir}/y_test.csv").values.ravel()

            model = RandomForestRegressor(
                n_estimators=self.n_estimators,
                random_state=42
            )

            model.fit(X_train, y_train)

            preds = model.predict(X_test)
            rmse = root_mean_squared_error(y_test, preds)

            logger.info(f"RMSE: {rmse:.4f}")

            os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
            joblib.dump(model, self.model_path)

            logger.info("Model saved successfully")

            return model
        
        except Exception as e:
            logger.error(f"Error during model training: {e}")
            raise e