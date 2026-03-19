import sys
import os
from src.exception import CustomError
from src.logger_file import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
@dataclass
class DataIngestionConfig:  #this class is used for making files or defining file path where train,test and raw datas exist
    train_data_path: str = os.path.join('artifacts','train_data.csv')
    test_data_path: str = os.path.join('artifacts','test_data.csv')
    raw_data_path: str = os.path.join('artifacts','raw_data.csv')


class DataIngestion:  #this class is used for reading dataset and split into train and test dataset then store into their relative paths , which were defined above
    def __init__(self):
        self.config = DataIngestionConfig()  #for the filepaths of train,test and raw datasets
    def initiate_dataingestion(self): #this object ingest the datas into their corresponding paths
        try:
            logging.info('DataIngestion initiated')
            os.makedirs(os.path.dirname(self.config.raw_data_path), exist_ok=True)
            df = pd.read_csv(os.path.join('notebook','data','ai_job_market.csv'))  #reading the dataset
            logging.info('Read the dataset')
            df.to_csv(self.config.raw_data_path, index=False, header = True)
            train_data,test_data = train_test_split(df,test_size=0.2,random_state=42)
            logging.info('Orginal data splitted into train and test dataset')
            train_data.to_csv(self.config.train_data_path, index=False, header=True)
            test_data.to_csv(self.config.test_data_path, index=False, header=True)
            logging.info('Train and test dataset saved into their relative paths')
            return self.config.train_data_path,self.config.test_data_path

        except Exception as e:
            raise CustomError(e,sys)

if __name__ == '__main__':
    ingestion = DataIngestion()  #creating an object
    ingestion.initiate_dataingestion()  #calling the method