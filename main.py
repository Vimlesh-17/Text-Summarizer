from src.TextSummarizer.logging import logger
from src.TextSummarizer.pipeline.stage_01_pipeline import DataIngestionTrainingPipeline
from src.TextSummarizer.pipeline.stage_02_pipeline import DataValidationTrainingPipeline

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


STAGE_NAME = "Data Validation Step"


try:
    logger.info(f">>> stage {STAGE_NAME} started <<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<<")
except Exception as e:
    logger.exception(e)
    raise e