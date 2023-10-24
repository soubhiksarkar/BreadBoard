from simple_project import logger
from simple_project.pipeline.block_01_data_ingestion import DataIngestionTrainingPipeline

BLOCK_NAME = "Data Ingestion Block"
try:
    logger.info(f">>>>>> block {BLOCK_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> block {BLOCK_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
