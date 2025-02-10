from src.datascience import logger
from src.datascience.pipeline.data_ingestion_01 import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
STAGE_NAME = "DATA_INGESTION_STAGE"
try:
    logger.info(f"{STAGE_NAME} is Started")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f"{STAGE_NAME} Completed")
except Exception as e:
    raise e

STAGE_NAME = "Validation Stage"
try:
    logger.info(f"{STAGE_NAME} Started")
    obj = DataValidationTrainingPipeline()
    obj.data_validation_pipeline()
    logger.info(f"{STAGE_NAME} is completed")
except Exception as e:
    raise e

