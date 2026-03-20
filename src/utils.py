import os 
import sys
from src.exception import CustomError
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import dill
def save_object(file_path,obj):  #this function is used for saving the preprocessor object into a file
    try:
        dir_path = os.path.dirname(file_path)  #getting the directory path from the file path
        os.makedirs(dir_path, exist_ok=True)  #creating the directory if it does not exist
        with open(file_path,'wb') as file_obj:  #opening the file in write binary mode
            dill.dump(obj,file_obj)  #dumping the object into the file
    except Exception as e:
        raise CustomError(e,sys)
    


def model_evaluation(X_train,y_train,X_test,y_test,models,params):  #this function is used for evaluating the models and returning the best model name and best model score
    try:
        model_report = {}
        trained_models = {}
        for model_name,model in models.items():
            param_grid = params[model_name]  #getting the parameters for the model from the params dictionary
            grid_search = GridSearchCV(estimator=model,param_grid=param_grid,cv=5,scoring='r2',n_jobs=-1)  #creating a GridSearchCV object for hyperparameter tuning
            grid_search.fit(X_train,y_train)  #training the model on the train data
            
            best_model = grid_search.best_estimator_  #getting the best model from the grid search, and the best model is for the current algorithm in the loop
            trained_models[model_name] = best_model  #storing the best model in the trained models dictionary with the model name as the key
            y_pred = best_model.predict(X_test) #predicting the target variable on the test data
            final_r2_score = r2_score(y_test,y_pred)
            
            model_report[model_name] = final_r2_score
           
        best_model_score = max(model_report.values())  #getting the best model score from the model report
        best_model_name = [model_name for model_name,score in model_report.items() if score == best_model_score][0]  #getting the best model name from the model report
        best_model = trained_models[best_model_name]  #getting the best model from the models dictionary or amoong the models of various algorithms
        return best_model,best_model_score
    except Exception as e:
        raise CustomError(e,sys)



def load_object(file_path):  #this function is used for loading the object from the file
    try:
        with open(file_path,'rb') as file_obj:  #opening the file in read binary mode
            return dill.load(file_obj)  #loading the object from the file and returning it
    except Exception as e:
        raise CustomError(e,sys)


if __name__=="__main__":
    print(load_object(os.path.join('artifacts','model.pkl')))