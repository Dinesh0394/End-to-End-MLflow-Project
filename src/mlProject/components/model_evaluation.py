import os
import pandas as pd
import numpy as np
from mlProject import logger
from mlProject.config.configuration import ModelEvaluationConfig
from sklearn.metrics import mean_squared_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import joblib
from mlProject.utils.common import save_json
from pathlib import Path


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    
    def eval_metrics(self, actual, predicted):
        """
        Calculate evaluation metrics: RMSE and R2 score.
        """
        rmse = np.sqrt(mean_squared_error(actual, predicted))
        mae = np.mean(np.abs(actual - predicted))
        r2 = r2_score(actual, predicted)
        return rmse, mae, r2
    
    def log_into_mlflow(self):
        testing_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = testing_data.drop(columns=[self.config.target_column], axis=1)
        test_y = testing_data[self.config.target_column]

        mlflow.set_tracking_uri(self.config.mlflow_uri)
        tracking_uri_type_store = urlparse(self.config.mlflow_uri).scheme  # to do everything inside the remote server we are using this

        with mlflow.start_run():
            predicted = model.predict(test_x)

            (rmse,mae,r2) = self.eval_metrics(test_y, predicted)

            scores = {
                "rmse": rmse,
                "mae": mae,
                "r2": r2
            }

            save_json(
                file_path=os.path.join(self.config.root_dir, self.config.metric_file_name),
                data=scores
            )

            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)


            if tracking_uri_type_store != "file":
                mlflow.sklearn.log_model(
                    sk_model=model,
                    artifact_path="model",
                    registered_model_name="ElasticnetModel"
                                    )   
            else:
                mlflow.sklearn.log_model(
                    sk_model=model,
                    artifact_path=os.path.join(self.config.root_dir, "model")
                )