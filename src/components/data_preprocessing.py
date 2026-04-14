from src.constants.config import config
from src.logger import get_logger
from sklearn.model_selection import train_test_split
import pandas as pd
import os

logger = get_logger(__name__)



class DataProcessing:

    def __init__(self):
        self.processed_dir = config["artifacts"]["processed_dir"]
        self.test_size = config["data"]["test_size"]
        self.random_state = config["data"]["random_state"]

    def run(self, raw_path):
        
        try:
            logger.info("Starting data processing")

            df = pd.read_csv(raw_path)

            X = df.drop("target", axis=1)
            y = df["target"]

            X_train, X_test, y_train, y_test = train_test_split(
                X, y,
                test_size=self.test_size,
                random_state=self.random_state
            )

            os.makedirs(self.processed_dir, exist_ok=True)

            X_train.to_csv(f"{self.processed_dir}/X_train.csv", index=False)
            X_test.to_csv(f"{self.processed_dir}/X_test.csv", index=False)
            y_train.to_csv(f"{self.processed_dir}/y_train.csv", index=False)
            y_test.to_csv(f"{self.processed_dir}/y_test.csv", index=False)

            logger.info("Data processing completed")
            
            return self.processed_dir
        
        except Exception as e:
            logger.error(f"Error during data processing: {e}")
            raise e

