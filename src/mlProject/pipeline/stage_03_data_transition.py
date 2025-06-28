from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation import DataTransformation
from mlProject import logger
from pathlib import Path


STAGE_NAME = "Data Validation Stage"


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path(r'D:\Dibu\Course_Notes\End-to-End-MLflow-Project\artifacts\data_validation\status.txt'), 'r') as file:
                status = file.read().strip().split(" ")[-1]

                if status == "True":
                    logger.info("Data validation passed. Proceeding to data transformation.")
                    config_manager = ConfigurationManager()
                    data_transformation_config = config_manager.get_data_transformation_config()
                    data_transformation = DataTransformation(config=data_transformation_config)
                    data_transformation.train_test_split()


                else:
                    logger.error("Data validation failed. Stopping the pipeline.")
                    return
                
        except FileNotFoundError as e:
            logger.error(f"Status file not found: {e}")
            raise e



if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<")
        pipeline = DataTransformationTrainingPipeline()
        pipeline.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:  
        logger.exception(e)
        raise e