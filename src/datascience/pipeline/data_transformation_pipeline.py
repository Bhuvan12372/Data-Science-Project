from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation
from src.datascience import logger
from pathlib import Path

STAGE_NAME = 'Data Transformation'

class DataTransformationOnPipeline:
    def __init__(self):
        pass
    def data_transformation_pipeline(self):
        try:
            with open(Path('artifacts/data_validation/statuses.txt'),'r') as f:
                status = f.read().split(" ")[-1]
            if status == "True":                                                #Giving here in string because it is in txt file
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config= data_transformation_config)
                data_transformation.train_test_split()
            else:
                raise Exception("Your column names or the data type of the columns are not matching, check and update it")
        except Exception as e:
            raise e


        