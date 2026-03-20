import os
import pandas as pd
import sys
from src.logger_file import logging
from src.exception import CustomError
from src.utils import load_object
from typing import Union
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

class CustomData:
    def __init__(self, 
                 job_title: Union[str, None] = None, 
                 company_size: Union[str, None] = None, 
                 company_industry: Union[str, None] = None, 
                 country: Union[str, None] = None, 
                 remote_type: Union[str, None] = None, 
                 experience_level: Union[str, None] = None, 
                 education_level: Union[str, None] = None, 
                 hiring_urgency: Union[str, None] = None,
                 years_experience: Union[int, None] = None, 
                 skills_python: int = 0,
                 skills_sql: int = 0, 
                 skills_ml: int = 0, 
                 skills_deep_learning: int = 0, 
                 skills_cloud: int = 0, 
                 job_posting_month: Union[int, None] = None, 
                 job_posting_year: Union[int, None] = None, 
                 job_openings: Union[int, None] = None):

        self.job_title = job_title
        self.company_size = company_size
        self.company_industry = company_industry
        self.country = country
        self.remote_type = remote_type
        self.experience_level = experience_level
        self.education_level = education_level
        self.hiring_urgency = hiring_urgency
        self.years_experience = years_experience
        self.skills_python = skills_python
        self.skills_sql = skills_sql
        self.skills_ml = skills_ml
        self.skills_deep_learning = skills_deep_learning
        self.skills_cloud = skills_cloud
        self.job_posting_month = job_posting_month
        self.job_posting_year = job_posting_year
        self.job_openings = job_openings

    def get_data_as_dataframe(self):
        try:
            data_dict = {
                'job_title': [self.job_title],
                'company_size': [self.company_size],
                'company_industry': [self.company_industry],
                'country': [self.country],
                'remote_type': [self.remote_type],
                'experience_level': [self.experience_level],
                'education_level': [self.education_level],
                'hiring_urgency': [self.hiring_urgency],
                'years_experience': [self.years_experience],
                'skills_python': [self.skills_python],
                'skills_sql': [self.skills_sql],
                'skills_ml': [self.skills_ml],
                'skills_deep_learning': [self.skills_deep_learning],
                'skills_cloud': [self.skills_cloud],
                'job_posting_month': [self.job_posting_month],
                'job_posting_year': [self.job_posting_year],
                'job_openings': [self.job_openings]
            }
            df = pd.DataFrame(data_dict)  #converting into dataframe
            return df
        except Exception as e:
            raise CustomError(e, sys)    

