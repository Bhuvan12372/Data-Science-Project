from src.datascience.constants import *
from src.datascience.utils.common import read_yaml,create_directories
from src.datascience.entity.config_entity import DataIngestionConfig
from src.datascience.entity.config_entity import DataValidationConfig
from src.datascience.entity.config_entity import DataTransformationConfig
from src.datascience.entity.config_entity import ModelTrainerConfig
from src.datascience.entity.config_entity import ModelEvaluationConfig

class ConfigurationManager:
    def __init__(self,config_filepath= CONFIG_FILE_PATH, params_filepath= PARAMS_FILE_PATH, schema_filepath = SCHEMA_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_directory = config.unzip_directory
        )
        return data_ingestion_config    
        
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS
        create_directories([config.root_dir])
        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            unzip_data_dir = config.unzip_data_dir,
            STATUS_FILE = config.STATUS_FILE,
            all_schema = schema
            )
        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])
        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_path = config.data_path
            )
        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_training
        params = self.params.ELASTIC_NET
        schema = self.schema.TARGET_COLUMN
        create_directories([config.root_dir])
        model_trainer_config = ModelTrainerConfig(
            root_dir = config.root_dir,
            training_data = config.training_data,
            testing_data = config.testing_data,
            model_name = config.model_name,
            alpha = params.alpha,
            l1_ratio = params.l1_ratio,
            target_column = schema

        )
        return model_trainer_config
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        schema = self.schema.TARGET_COLUMN
        params = self.params.ELASTIC_NET
        create_directories([config.root_dir])
        model_evaluation_config = ModelEvaluationConfig(
            root_dir = config.root_dir,
            test_path = config.test_path,
            model_path= config.model_path,
            evaluate_path = config.evaluate_path,
            all_params = params,
            target_column = schema,
            mlflow_uri = "https://dagshub.com/bhuvankatakam/Data-Science-Project.mlflow"
            )
        return model_evaluation_config
    



    

    
