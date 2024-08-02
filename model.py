import uvicorn
from fastapi import FastAPI
import pickle
from pydantic import BaseModel
import pandas as pd
import numpy as np
import sklearn
from sklearn.ensemble import RandomForestClassifier
import json
# 2. Create the app object
from fastapi.middleware.cors import CORSMiddleware

# Add CORS middleware to allow requests from all origins

class Smart(BaseModel):
    	 		
    Type: int
    Air_temperature: float
    Process_temperature: float
    Rotational_speed : float
    Torque_NM: float
    Tool_wear_min:float

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],

    allow_methods=["*"],
    allow_headers=["*"],
)
def Final():
    with open("maint.pickle4","rb") as f:
        classifier=pickle.load(f)
    return classifier

@app.get('/')
def index():
    return {'message': 'Hello, World'}


@app.post('/predict')
def predict(data: Smart):
    Type= data.Type
    Air_temperature= data.Air_temperature
    Process_temperature=data.Process_temperature
    Rotational_speed = data.Rotational_speed
    Torque_NM= data.Torque_NM
    Tool_wear_min=data.Tool_wear_min
    x=[[ Type,
    Air_temperature,
    Process_temperature,
    Rotational_speed,
    Torque_NM,
    Tool_wear_min]]
    prediction =Final().predict(x)
    if(prediction[0]==1):
        prediction="Machine Can Fail"
    else:
        prediction="Machine Has Life"
    return {
        'prediction': prediction
    }