from src.TextSummarizer.logging import logger
from src.TextSummarizer.pipeline.stage_01_pipeline import DataIngestionTrainingPipeline

# logger.info("Welcome to the cult")
STAGE_NAME = "Data Ingestion Step"

try:
    logger.info(f">>> stage {STAGE_NAME} started <<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<<")
except Exception as e:
    logger.exception(e)
    raise e