from fastapi import FastAPI
from prediction import Prediction
from joblib import dump, load

app = FastAPI()
model = load("model.ml")

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/wel")
def get_name(name:str):
    return{"wlecpme to my page" : f'{name}'}

@app.post("/predict")
def predict_placement(data:Prediction):
    data = data.dict()
    aggregate=data["aggregate"]
    technical=data["technical"]
    communication=data["communication"]
    backlog=data["backlogs"]
    value = model.predict([[aggregate,technical,communication,backlog]])[0]
    return f'{value}'
