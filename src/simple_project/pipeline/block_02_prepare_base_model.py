from simple_project.config.configuration import ConfigurationManager
from simple_project.components.prepare_base_model import PrepareBaseModel
from simple_project import logger


BLOCK_NAME = "Prepare Base Model Block"


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


    
if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> block {BLOCK_NAME} started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> block {BLOCK_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
