from simple_project import logger
from simple_project.pipeline.block_01_data_ingestion import DataIngestionTrainingPipeline
from simple_project.pipeline.block_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from simple_project.pipeline.block_03_model_training import ModelTrainingPipeline

BLOCK_NAME = "Data Ingestion Block"
try:
    logger.info(f">>>>>> block {BLOCK_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> block {BLOCK_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

BLOCK_NAME = "Prepare Base Model Block"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> block {BLOCK_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> block {BLOCK_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

BLOCK_NAME = "Training"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> block {BLOCK_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> block {BLOCK_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
