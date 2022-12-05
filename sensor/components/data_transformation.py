from sensor.entity import artifact_entity,config_entity
from sensor.exception import SensorException
from sensor.logger import logging
from typing import Optional
import os,sys 
import pandas as pd
from sensor import utils
import numpy as np
from sensor.config import TARGET_COLUMN


class DataTransformation:
    def __init__(self,
                data_transformation_config:config_entity.DataTransformationConfig,
                data_ingestion_artifact : artifact_entity.DataIngestionArtifact)
      
        try:
            self.data_transformation_config = data_transformation_config
            self.data_ingestion_artifact = data_ingestion_artifact

        except Exception as e :
            raise SensorException(e,sys)

    @classmethod
    def get_data_transformer_object(cls):
        try:
            
        except Exception as e :
            raise SensorException(e,sys)
