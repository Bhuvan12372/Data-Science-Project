from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_validation import DataValidation
from src.datascience import logger

STAGE_NAME = 'Validation Stage'

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    def data_validation_pipeline(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config = data_validation_config)
        data_validation.validate_all_columns()


if __name__ == '__main__':
    try:
        logger.info(f"{STAGE_NAME} Started")
        obj = DataValidationTrainingPipeline()
        obj.data_validation_pipeline()
        logger.info(f"{STAGE_NAME} is completed")
    except Exception as e:
        raise e
    


