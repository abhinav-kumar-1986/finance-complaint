from finance_complaint.exception import FinanceException
from finance_complaint.logger import logger
from finance_complaint.config.pipeline.training import FinanceConfig
from finance_complaint.component.training import DataIngestion
from finance_complaint.entity.artifact_entity import DataIngestionArtifact

import sys


class TrainingPipeline:

    def __init__(self, finance_config: FinanceConfig):
        self.finance_config: FinanceConfig = finance_config

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion_config = self.finance_config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            return data_ingestion_artifact

        except Exception as e:
            raise FinanceException(e, sys)
        
    def start(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise FinanceException(e, sys)