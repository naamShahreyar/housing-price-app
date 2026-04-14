from src.components.data_ingestion import DataIngestion
from src.components.data_preprocessing import DataProcessing
from src.components.model_trainer import ModelTrainer

from src.logger import get_logger

logger = get_logger(__name__)


def run_pipeline():
    try:
        logger.info("Pipeline started")

        ingestion = DataIngestion()
        raw_path = ingestion.run()

        processing = DataProcessing()
        processed_dir = processing.run(raw_path)

        trainer = ModelTrainer()
        trainer.run(processed_dir)

        logger.info("Pipeline completed")
        
    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        raise e


if __name__ == "__main__":
    run_pipeline()