import os
import mlflow
import mlflow.sklearn
import pandas as pd
from urllib.parse import urlparse
import numpy as np
import joblib
from src.datascience.config.configuration import ModelEvaluationConfig
from sklearn.metrics import r2_score,mean_squared_error, mean_absolute_error
from src.datascience.utils.common import read_yaml,create_directories,save_json
from pathlib import Path

class ModelEvaluation:
    def __init__(self,config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self,actual,pred):
        mse = mean_absolute_error(actual,pred)
        rmse =  np.sqrt(mse)
        mae = mean_absolute_error(actual,pred)
        r2 = r2_score(actual,pred)
        return mse,rmse,mae,r2
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_path)
        target_column = list(self.config.target_column.keys())[0]
        test_x = test_data.drop([target_column],axis = 1)
        test_y = test_data[[target_column]]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_uri_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        with mlflow.start_run():
            model = joblib.load(self.config.model_path)
            predicted_qualities = model.predict(test_x)
            (mse,rmse,mae,r2) = self.eval_metrics(test_y,predicted_qualities)
            scores = {"mse" : mse, "rmse": rmse, "mae": mae, "r2_score" : r2}
            save_json(path = Path(self.config.evaluate_path),data= scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("mse", mse)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            # Model Registry does not work with file store
            if tracking_uri_type_store != "file":
                mlflow.sklearn.log_model(model,"model", registered_model_name= "ELASTICNET")
            else:
                mlflow.sklearn.log_model(model,"model")


    
        
