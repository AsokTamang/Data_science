import sys
import os
from dataclasses import dataclass
from sklearn.model_selection import train_test_split, cross_val_score
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.tree import DecisionTreeRegressor
from src.utils import save_object
from src.logger_file import logging
from src.exception import CustomError
from src.components.data_transformation import DataTransformation
from src.components.data_ingestion import DataIngestion
from src.utils import model_evaluation, save_object


dataingestion = DataIngestion()
 # creating an object for data ingestion class to get the train and test data paths
train_data_path = dataingestion.initiate_dataingestion()[
    0
]  # getting the train data path from the data ingestion class
test_data_path = dataingestion.initiate_dataingestion()[
    1
]  # getting the test data path from the data ingestion class
datatransformation = DataTransformation()  # creating an object for data transformation class to get the preprocessor object file path
train_data_array,test_data_array,processor_filepath = datatransformation.initiate_data_transformation(train_data_path, test_data_path)  # calling the method to get the preprocessor object file path


@dataclass
class ModelTrainerConfig:  # this class is used for defining the file path where the trained model will be saved
    trained_model_file_path: str = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self):
        self.config = ModelTrainerConfig()  # for the file path where the trained model will be saved

    def initiate_model_trainer(self, train_array, test_array):
        try:
                logging.info("Model training initiated")
                X_train, y_train = train_array[:, :-1], train_array[:, -1]
                X_test, y_test = test_array[:, :-1], test_array[:, -1]
                models = {
                    "Linear Regression": LinearRegression(),
                    "Random Forest": RandomForestRegressor(),
                    "Gradient Boosting": GradientBoostingRegressor(),
                    "XGBRegressor": XGBRegressor(),
                    "Decision Tree": DecisionTreeRegressor(),
                }
                #parameters for hyperparameter tuning based on each model
                params = {
                    "Linear Regression": {},
                    "Random Forest": {
                        "n_estimators": [100, 200],
                        "max_depth": [None, 10, 20],
                    },
                    "Gradient Boosting": {
                        "n_estimators": [100, 200],
                        "learning_rate": [0.05,0.01,0.1],
                    },
                    "XGBRegressor": {
                        "n_estimators": [100, 200],
                        "learning_rate": [0.01, 0.1],
                    },
                    "Decision Tree": {"max_depth": [None, 10, 20]},
                }
                best_model,best_model_score = model_evaluation(X_train, y_train, X_test, y_test, models,params)
                logging.info(f"Best model found on both training and testing dataset with score of {best_model_score}")
                save_object(file_path=self.config.trained_model_file_path, obj=best_model)
                logging.info(f"Trained model saved at {self.config.trained_model_file_path}")
                return best_model , best_model_score
        except Exception as e:
            raise CustomError(e, sys)

if __name__ == "__main__":
    trainer = ModelTrainer()  # creating an object for model trainer class
    print(trainer.initiate_model_trainer(train_data_array, test_data_array))  # calling the method to train the model and get the best model name and best model score