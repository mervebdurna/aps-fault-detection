from sensor.entity import artifact_entity,config_entity
from sensor.exception import SensorException
from sensor.logger import logging
from scipy.stats import ks_2samp
from typing import Optional
import os,sys 
import pandas as pd
from sensor import utils
import numpy as np



class DataValidation:
    def __init__(self,
                data_validation_config : config_entity.DataValidationConfig,
                data_ingestion_artifact : artifact_entity.DataIngestionArtifact ):
        try:
            logging.info(f"{'>>'*20} Data Validation {'<<'*20}")
            self.data_validation_config=data_validation_config
            self.data_ingestion_artifact=data_ingestion_artifact
            self.validation_error = dict()
        except Exception as e:
            raise SensorException(e,sys)
    

    def drop_missing_values_columns(self, df:pd.DataFrame, report_key_name:str) -> Optional[pd.DataFrame]:
        """"
        This function will drop column which contains missing value more than specified threshold
        
        
        Parameters :
        ------------

        df :




        Returns:
        --------



        
        """
        pass

    def is_required_column_exists():
        pass

    def data_drift():
        pass

    def initiate_data_validation():
        pass


