import pandas as pd
import os
from src.datascience import logger
from sklearn.linear_model import ElasticNet
import joblib
from src.datascience.entity.config_entity import ModelTrainerConfig
class ModelTrainer:
    def __init__(self,config: ModelTrainerConfig):
        self.config  = config
    
    def train(self):
        train_data = pd.read_csv(self.config.training_data)
        test_data = pd.read_csv(self.config.testing_data)
        train_x = train_data.drop(columns = ['quality'],axis = 1)
        test_x = test_data.drop(columns = ['quality'],axis = 1)
        train_y = train_data['quality']
        test_y = test_data['quality']
        lr = ElasticNet(alpha = self.config.alpha,l1_ratio = self.config.l1_ratio,random_state = 42)
        joblib.dump(lr,os.path.join(self.config.root_dir,self.config.model_name))

