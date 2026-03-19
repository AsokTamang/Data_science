import sys
import os
import pandas as pd
from sklearn.compose import ColumnTransformer
from src.logger_file import logging
from src.exception import CustomError
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.pipeline import Pipeline
from dataclasses import dataclass
from sklearn.impute import SimpleImputer
from src.components.data_ingestion import DataIngestion
import numpy as np
from src.utils import save_object


dataingestion = (
    DataIngestion()
)  # creating an object for data ingestion class to get the train and test data paths
train_data_path = dataingestion.initiate_dataingestion()[
    0
]  # getting the train data path from the data ingestion class
test_data_path = dataingestion.initiate_dataingestion()[
    1
]  # getting the test data path from the data ingestion class


@dataclass
class DataTransformationConfig:  # this class is used for making a filepath for our preprocessor object
    preprocessor_obj_filepath: str = os.path.join("artifacts", "preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.config = DataTransformationConfig()

    def get_data_transformer_obj(self):
        try:
            numerical_features = [
                "years_experience",
                "skills_python",
                "skills_sql",
                "skills_ml",
                "skills_deep_learning",
                "skills_cloud",
                "job_posting_month",
                "job_posting_year",
                "job_openings",
            ]
            nominal_categorical_features = [
                "job_title",
                "company_industry",
                "country",
                "remote_type",
                "company_size",
            ]  # has no order within them
            ordinal_categorical_features = [
                "experience_level",
                "education_level",
                "hiring_urgency",
            ]  # has orders within them

            experience_order = ["Entry", "Mid", "Senior"]  # 0, 1, 2
            education_order = ["Bachelor", "Master", "PhD"]  # 0, 1, 2
            hiring_urgency_order = ["Low", "Medium", "High"]

            num_pipeline = Pipeline(
                [
                    (
                        "imputer",
                        SimpleImputer(strategy="median"),
                    ),  # for filling the null values
                    ("scalar", StandardScaler()),  # for standard scaling
                ]
            )
            logging.info("Numerical pipeline created successfully")

            nominal_cat_pipeline = Pipeline(
                [
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("encoder", OneHotEncoder(sparse_output=False)),  # for one hot encoding the nominal categorical features, as it always return the sparse matrix, we have to set the sparse_output to False to get the array output
                ]
            )
            logging.info("Nominal categorical pipeline created successfully")

            ordinal_cat_pipeline = Pipeline(
                [
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    (
                        "encoder",
                        OrdinalEncoder(
                            categories=[
                                experience_order,
                                education_order,
                                hiring_urgency_order,
                            ]
                        ),
                    ),
                ]
            )
            logging.info("Ordinal categorical pipeline created successfully")

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_features),
                    (
                        "nominal_cat_pipeline",
                        nominal_cat_pipeline,
                        nominal_categorical_features,
                    ),
                    (
                        "ordinal_cat_pipeline",
                        ordinal_cat_pipeline,
                        ordinal_categorical_features,
                    ),
                ]
            )
            logging.info("Column transformer created successfully")
            return preprocessor
        except Exception as e:
            raise CustomError(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            # reading the train and test data from their relative paths
            train_data_df = pd.read_csv(train_path)
            test_data_df = pd.read_csv(test_path)
            logging.info("Train and test data read successfully")

            preprocessor_obj = self.get_data_transformer_obj()
            logging.info("Preprocessor object obtained successfully")

            target_column = "salary"
            X_train = train_data_df.drop(columns=[target_column])
            y_train = train_data_df[target_column]
            X_test = test_data_df.drop(columns=[target_column])
            y_test = test_data_df[target_column]
            logging.info(
                "Train and test data split into features and target variable successfully"
            )

            X_train_transformed = preprocessor_obj.fit_transform(
                X_train
            )  # this returns the array after applying the transformations on the train data
            X_test_transformed = preprocessor_obj.transform(X_test)

            logging.info("Train and test data transformed successfully")
            train_array = np.c_[
                X_train_transformed, y_train
            ]  # this is used for concatenating the transformed features and target variable into a single array for the train data
            test_array = np.c_[
                X_test_transformed, y_test
            ]  # this is used for concatenating the transformed features and target variable into a single array for the test data

            save_object(
                file_path=self.config.preprocessor_obj_filepath, obj=preprocessor_obj
            )  # this is used for saving the preprocessor object into a file
            logging.info("Preprocessor object saved successfully")

            return train_array, test_array, self.config.preprocessor_obj_filepath

        except Exception as e:
            raise CustomError(e, sys)


if __name__ == "__main__":
    obj = DataTransformation()
    obj.initiate_data_transformation(
        train_path=train_data_path, test_path=test_data_path
    )
