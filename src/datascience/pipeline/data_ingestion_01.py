from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_ingestion import DataIngestion
from src.datascience import logger



STAGE_NAME = "DATA INGESTION STAGE"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def initiate_data_ingestion(self):
        config = ConfigurationManager()
        get_data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = get_data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f"{STAGE_NAME} is Started")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f"{STAGE_NAME} Completed")
    except Exception as e:
        raise e