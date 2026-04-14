from src.constants.config import config
from src.logger import get_logger
from sklearn.datasets import fetch_california_housing
import os
import pandas as pd

logger = get_logger(__name__)

class DataIngestion:

    def __init__(self):
        self.raw_path = config["artifacts"]["raw_data"]

    def run(self):
        
        try:
            logger.info("Starting data ingestion")

            os.makedirs(os.path.dirname(self.raw_path), exist_ok=True)

            data = fetch_california_housing(as_frame=True)
            df = pd.concat([data.data, data.target.rename("target")], axis=1)

            df.to_csv(self.raw_path, index=False)

            logger.info(f"Data saved to {self.raw_path}")
            
            return self.raw_path
        except Exception as e:
            logger.error(f"Error during data ingestion: {e}")
            raise e

