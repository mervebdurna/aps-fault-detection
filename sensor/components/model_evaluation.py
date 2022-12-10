from sensor.predictor import ModelResolver
from sensor.entity import config_entity,artifact_entity
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.utils import load_object
from sklearn.metrics import f1_score
import pandas  as pd
import sys,os
from sensor.config import TARGET_COLUMN
class ModelEvaluation:

    def __init__(self,
        model_eval_config:config_entity.ModelEvaluationConfig,
        data_ingestion_artifact:artifact_entity.DataIngestionArtifact,
        data_transformation_artifact:artifact_entity.DataTransformationArtifact,
        model_trainer_artifact:artifact_entity.ModelTrainerArtifact      
        ):
        try:
            logging.info(f"{'>>'*20}  Model Evaluation {'<<'*20}")
            self.model_eval_config=model_eval_config
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_transformation_artifact=data_transformation_artifact
            self.model_trainer_artifact=model_trainer_artifact
            self.model_resolver = ModelResolver()
        except Exception as e:
            raise SensorException(e,sys)



    def initiate_model_evaluation(self)->artifact_entity.ModelEvaluationArtifact:
        try:
            #if saved model folder has model the we will compare 
            #which model is best trained or the model from saved model folder

            logging.info("Compare the current model with the last saved model. Save current model if there is no saved model in the directory.")
            latest_dir_path = self.model_resolver.get_latest_dir_path()
            if latest_dir_path==None:
                model_eval_artifact = artifact_entity.ModelEvaluationArtifact(is_model_accepted=True,
                improved_accuracy=None)
                logging.info(f"Model evaluation artifact: {model_eval_artifact}")
                return model_eval_artifact


            logging.info("Finding location of latest transformer, target encoder and model")
            transformer_path = self.model_resolver.get_latest_transformer_path()
            target_encoder_path = self.model_resolver.get_latest_target_encoder_path()
            model_path = self.model_resolver.get_latest_model_path()

            logging.info("Get lastest transformer, target encoder and model objects")
            transformer = load_object(file_path=transformer_path)
            target_encoder = load_object(file_path=target_encoder_path)
            model = load_object(file_path=model_path)
            
            

            logging.info("Get current transformer, target encoder and model objects")
            current_transformer = load_object(file_path=self.data_transformation_artifact.transform_object_path)
            current_target_encoder = load_object(file_path=self.data_transformation_artifact.target_encoder_path)
            current_model  = load_object(file_path=self.model_trainer_artifact.model_path)
            
            

            logging.info("Read test data from data_ingestion_artifact")
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)

            logging.info("Extract target from test_df. Apply target_encoder.")
            target_df = test_df[TARGET_COLUMN]
            y_true =target_encoder.transform(target_df)
            
            
            logging.info(f"Checking latest trained model accuracy")
            input_feature_name = list(transformer.feature_names_in_)
            input_arr =transformer.transform(test_df[input_feature_name])
            y_pred = model.predict(input_arr)
            print(f"Prediction using latest trained model: {target_encoder.inverse_transform(y_pred[:5])}")
            latest_model_score = f1_score(y_true=y_true, y_pred=y_pred)
            logging.info(f"Accuracy using latest trained model: {latest_model_score}")
           
            logging.info(f"Checking current trained model accuracy")
            input_feature_name = list(current_transformer.feature_names_in_)
            input_arr =current_transformer.transform(test_df[input_feature_name])
            y_pred = current_model.predict(input_arr)
            y_true =current_target_encoder.transform(target_df)
            print(f"Prediction using current trained model: {current_target_encoder.inverse_transform(y_pred[:5])}")
            current_model_score = f1_score(y_true=y_true, y_pred=y_pred)
            logging.info(f"Accuracy using current trained model: {current_model_score}")
            
            logging.info(f"Compare latest and current trained model")
            if current_model_score<=latest_model_score:
                logging.info(f"Current trained model is not better than latest model")
                raise Exception("Current trained model is not better than latest model")

            model_eval_artifact = artifact_entity.ModelEvaluationArtifact(is_model_accepted=True,
            improved_accuracy=current_model_score-latest_model_score)
            logging.info(f"Model eval artifact: {model_eval_artifact}")
            return model_eval_artifact
        
        except Exception as e:
            raise SensorException(e,sys)
