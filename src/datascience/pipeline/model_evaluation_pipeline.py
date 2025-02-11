
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_evaluation import ModelEvaluation

STAGE_NAME = 'Validation Stage'

class ModelEvaluationonPipeline:
    def __init__(self):
        pass
    def model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluate = ModelEvaluation(model_evaluation_config)
        model_evaluate.log_into_mlflow()

