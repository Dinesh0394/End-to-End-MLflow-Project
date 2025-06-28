from dataclasses import dataclass
from pathlib import Path

#  This is just to ensure that the dataclass is defined correctly and it won't accept other than the specified types.
#  If you try to create an instance with a different type, it will raise a TypeError.
#  so we are telling the compiler to return only the specified types not any other types.
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


# Validation config for data validation stage

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict


# Data transformation config for data transformation stage
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path


# Model training config for model training stage
@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str

# Model evaluation config for model evaluation stage
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: str
    target_column: str
    mlflow_uri: str

