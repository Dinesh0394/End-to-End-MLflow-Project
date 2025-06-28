from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_training import ModelTraining
from mlProject import logger


STAGE_NAME = "Model Training Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config_manager = ConfigurationManager()
            model_training_config = config_manager.get_model_training_config()
            model_training_config = ModelTraining(config=model_training_config)
            model_training_config.train_model()

        except Exception as e:
            logger.exception(e)
            raise e
        


if __name__ == '__main__':    
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<")
        pipeline = ModelTrainingPipeline()
        pipeline.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e