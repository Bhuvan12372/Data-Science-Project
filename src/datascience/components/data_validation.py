import pandas as pd
from src.datascience import logger
from src.datascience.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self,config: DataValidationConfig):
        self.config = config
    
    def validate_all_columns(self) -> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation_Staus is {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation_Staus is {validation_status}")
        except Exception as e:
            raise e
        
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_col_datatypes = {col: data[col].dtype for col in data.columns}
            all_schema = self.config.all_schema  

            for col,col_dtype in all_col_datatypes.items():
                if col_dtype != all_schema.get(col,None):
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation_Staus is {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation_Staus is {validation_status}")
        except Exception as e:
            raise e



