from src.TextSummarizer.logging import logger
from src.TextSummarizer.pipeline.stage_01_pipeline import DataIngestionTrainingPipeline
from src.TextSummarizer.pipeline.stage_02_pipeline import DataValidationTrainingPipeline
from src.TextSummarizer.pipeline.stage_03_pipeline import DataTransformationTrainingPipeline
from src.TextSummarizer.pipeline.stage_04_pipeline import ModelTrainerTrainingPipeline

from src.TextSummarizer.pipeline.stage_05_pipeline import ModelEvaluationTrainingPipeline


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

STAGE_NAME = "Data Tranformation Step"


try:
    logger.info(f">>> stage {STAGE_NAME} started <<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer Step"


try:
    logger.info(f">>> stage {STAGE_NAME} started <<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation Step"


try:
    logger.info(f">>> stage {STAGE_NAME} started <<<")
    model_evaluator = ModelEvaluationTrainingPipeline()
    model_evaluator.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<<")
except Exception as e:
    logger.exception(e)
    raise e