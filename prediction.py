from pydantic import BaseModel
class Prediction(BaseModel):
    aggregate : int
    technical:int
    communication:int
    backlogs:int
