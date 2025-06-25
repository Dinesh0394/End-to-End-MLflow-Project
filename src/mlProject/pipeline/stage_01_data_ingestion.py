from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_ingestion import DataIngestion
from mlProject import logger


STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()


# since it's a OOPs concept we are calling then main function inside this if condition

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<")
        pipeline = DataIngestionTrainingPipeline()
        pipeline.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
    
#  if you want to test this, you have to use main function and run this file directly.