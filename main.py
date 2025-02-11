from src.datascience import logger
from src.datascience.pipeline.data_ingestion_01 import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationOnPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTraineronPipeline
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


STAGE_NAME = 'Data Transformation'
try:
    logger.info(f"{STAGE_NAME}Started")
    obj = DataTransformationOnPipeline()
    obj.data_transformation_pipeline()
    logger.info(f"{STAGE_NAME} is completed")
except Exception as e:
    raise e


STAGE_NAME = 'Model Trainer'
try:
    logger.info(f"{STAGE_NAME} is Started")
    obj = ModelTraineronPipeline()
    obj.model_training_pipeline()
    logger.info(f"{STAGE_NAME} is completed")
except Exception as e:
    raise e

