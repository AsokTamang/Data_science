import sys
import os

from sklearn.compose import ColumnTransformer

from src.logger_file import logging
from src.exception import CustomError
from sklearn.preprocessing import StandardScaler, OneHotEncoder , OrdinalEncoder
from sklearn.pipeline import Pipeline
from dataclasses import dataclass
from sklearn.impute import SimpleImputer

@dataclass
class DataTransformationConfig:  #this class is used for making a filepath for our preprocessor object
    preprocessor_obj_filepath:str = os.path.join('artifacts','preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.config = DataTransformationConfig()

    def get_data_transformer_obj(self):
        try:
            numerical_features =['years_experience', 'skills_python', 'skills_sql', 'skills_ml', 'skills_deep_learning', 'skills_cloud', 'job_posting_month', 'job_posting_year', 'job_openings']
            nominal_categorical_features = ['job_title', 'company_industry', 'country', 'remote_type',
                                            'company_size']  # has no order within them
            ordinal_categorical_features = ['experience_level', 'education_level',
                                            'hiring_urgency']  # has orders within them

            experience_order = ['Entry', 'Mid', 'Senior']  # 0, 1, 2
            education_order = ['Bachelor', 'Master', 'PhD']  # 0, 1, 2
            hiring_urgency_order = ['Low', 'Medium', 'High']

            num_pipeline = Pipeline([
                ('imputer', SimpleImputer(strategy='median')),  #for filling the null values
                ('scalar', StandardScaler()),     #for standard scaling
            ])

            nominal_cat_pipeline = Pipeline([
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('encoder', OneHotEncoder())
            ])

            ordinal_cat_pipeline = Pipeline([
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('encoder', OrdinalEncoder(
                    categories=
                    [
                        experience_order,education_order,hiring_urgency_order
                    ]
                ))
            ])

            preprocessor = ColumnTransformer(
                [
                    ('num_pipeline', num_pipeline, numerical_features),
                    ('nominal_cat_pipeline', nominal_cat_pipeline, nominal_categorical_features),
                    ('ordinal_cat_pipeline', ordinal_cat_pipeline, ordinal_categorical_features)
                ]
            )

            return preprocessor








        except Exception as e:
            raise CustomError(e,sys)

