import os
import sys
from src.exception import CustomError
from src.utils import load_object



class PredictPipeline:
    def __init__(self):
        pass
    def predict(self,features):
        try:
            preprocessor_path = os.path.join('artifacts','preprocessor.pkl')  #getting the preprocessor object file path
            model_path = os.path.join('artifacts','model.pkl')  #getting the model file path
            
            preprocessor = load_object(preprocessor_path)  #loading the preprocessor object from the file
            model = load_object(model_path)  #loading the model from the file
            
            data_scaled = preprocessor.transform(features)  #scaling the features using the preprocessor object
            pred = model.predict(data_scaled)  #predicting the target variable using the model
            
            return pred
        except Exception as e:
            raise CustomError(e,sys)

