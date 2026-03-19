import os 
import sys
from src.exception import CustomError
from src.logger_file import logging
import pickle
def save_object(file_path,obj):  #this function is used for saving the preprocessor object into a file
    try:
        dir_path = os.path.dirname(file_path)  #getting the directory path from the file path
        os.makedirs(dir_path, exist_ok=True)  #creating the directory if it does not exist
        with open(file_path,'wb') as file_obj:  #opening the file in write binary mode
            pickle.dump(obj,file_obj)  #dumping the object into the file
    except Exception as e:
        raise CustomError(e,sys)