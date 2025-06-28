import os
from mlProject import logger
from mlProject.config.configuration import ModelTrainingConfig
from sklearn.linear_model import ElasticNet
import pandas as pd
import joblib


class ModelTraining:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config

    def train_model(self) -> bool:
        training_data = pd.read_csv(self.config.train_data_path)
        testing_data = pd.read_csv(self.config.test_data_path)

        train_x = training_data.drop(columns=[self.config.target_column],axis=1)
        test_x = testing_data.drop(columns=[self.config.target_column],axis=1)
        train_y = training_data[self.config.target_column]
        test_y = testing_data[self.config.target_column]

        lr_model = ElasticNet(
            alpha=self.config.alpha,
            l1_ratio=self.config.l1_ratio
        )
        lr_model.fit(train_x, train_y)


        joblib.dump(lr_model, os.path.join(self.config.root_dir, self.config.model_name))