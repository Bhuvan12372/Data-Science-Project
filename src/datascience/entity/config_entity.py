from dataclasses import dataclass
from pathlib import Path
  
@dataclass                # No need of initiazling __init__
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_directory: Path

@dataclass
class DataValidationConfig:
    root_dir: Path
    unzip_data_dir: Path
    STATUS_FILE: str
    all_schema: dict   #schema.yaml configurations


@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path


@dataclass
class ModelTrainerConfig:
    root_dir: Path
    training_data: Path
    testing_data: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str


