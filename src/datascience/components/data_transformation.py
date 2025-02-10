import os
import pandas as pd
from src.datascience import logger
from sklearn.model_selection import train_test_split
from src.datascience.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self,config: DataTransformationConfig):
        self.config = config
    
    def train_test_split(self):
        data = pd.read_csv(self.config.data_path)
        train,test = train_test_split(data)
        train.to_csv(os.path.join(self.config.root_dir,"Train.csv"))
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"))
        logger.info("Spliitted data into train and test set")
        logger.info(train.shape)
        logger.info(test.shape)
        print(train.shape)
        print(test.shape)