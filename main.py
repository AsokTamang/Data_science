import sys
from src.exception import CustomError
from src.logger_file import logging
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from src.pipeline.predict_pipeline import PredictPipeline
from src.pipeline.data_validation_pipeline import CustomData
from pydantic import BaseModel
from typing import Union
import uvicorn

app = FastAPI()

app.mount('/static', StaticFiles(directory='statics'), name='statics')


@app.get('/')
def root():
    return FileResponse('statics/home.html')


# ✅ Pydantic model to receive JSON from your HTML form
class PredictRequest(BaseModel):
    job_title: Union[str, None] = None
    company_size: Union[str, None] = None
    company_industry: Union[str, None] = None
    country: Union[str, None] = None
    remote_type: Union[str, None] = None
    experience_level: Union[str, None] = None
    education_level: Union[str, None] = None
    hiring_urgency: Union[str, None] = None
    years_experience: Union[int, None] = None
    skills_python: int = 0
    skills_sql: int = 0
    skills_ml: int = 0
    skills_deep_learning: int = 0
    skills_cloud: int = 0
    job_posting_month: Union[int, None] = None
    job_posting_year: Union[int, None] = None
    job_openings: Union[int, None] = None


@app.get('/prediction_form')
def prediction_form():
    return FileResponse('statics/index.html')


@app.post('/predict')
def predict(data: PredictRequest): #the type of data is the pydantic model which we created above to receive the json data from the html form
    try:
        features = CustomData(
            job_title=data.job_title,
            company_size=data.company_size,
            company_industry=data.company_industry,
            country=data.country,
            remote_type=data.remote_type,
            experience_level=data.experience_level,
            education_level=data.education_level,
            hiring_urgency=data.hiring_urgency,
            years_experience=data.years_experience,
            skills_python=data.skills_python,
            skills_sql=data.skills_sql,
            skills_ml=data.skills_ml,
            skills_deep_learning=data.skills_deep_learning,
            skills_cloud=data.skills_cloud,
            job_posting_month=data.job_posting_month,
            job_posting_year=data.job_posting_year,
            job_openings=data.job_openings
        )

        df_features = features.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        result = predict_pipeline.predict(df_features)

        return {'prediction': float(result[0])}  #extracts [0] from numpy array

    except Exception as e:
        logging.error(f"Prediction error: {e}")
        raise CustomError(e, sys)
    

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 
