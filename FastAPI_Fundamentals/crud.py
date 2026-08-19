from fastapi import FastAPI,Path, HTTPException
from fastapi.responses import  JSONResponse
from pydantic import BaseModel,Field,computed_field
from typing import Annotated, Literal
import json
app = FastAPI()

class patient(BaseModel):
    id: Annotated[str, Field(..., description = "id of the patient", example = "P001")]
    name:Annotated[str, Field(..., description = "Name of the patient")]
    city:Annotated[str, Field(..., description = "city of the patient")]
    age: Annotated[int, Field(..., gt = 0, le = 120, description = "age of the poatient")]
    gender:Annotated[str, Literal['male','female','other'], Field(..., description = "Gender of the patient")]
    height:Annotated[float, Field(..., gt = 0, description="height of the patient in meters")]
    weight:Annotated[float, Field(..., gt = 0, description = "weight of the patient in kgs")]
    @computed_field
    @property
    def patient_bmi(self)->float:
        bmi = (self.weight) / (self.height)**2
        return bmi


    @computed_field
    @property
    def patient_verdict(self)->str:
        if self.patient_bmi < 18.5:
            return "underweight"

        elif self.patient_bmi < 25:
            return "Normal"
        elif self.patient_bmi < 30:
            return "Normal"
        else:
            return "Obese"



def load_data():
    with open("patients.json", 'r') as f:
        data = json.load(f)
    return data
data = load_data()

def save_data(data):
    with open("patients.json",'w') as f:
        json.dump(data,f)


@app.get('/')
def hello():
    return "Patient Management System"

@app.get('/about')
def about():
    return "this is a patient management systems which handles all patient related data"

@app.get("/view")
def view():
    return data


@app.get('/patient/{patient_id}')

def view_patient(patient_id:str =  Path(..., description = "ID of the patient in the DB", example = "P001")):
    data = load_data()
 
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code= 404, detail ="Patient not Found")  


@app.post('/create')
def create_patient(patient:patient):
    data = load_data()
    if patient.id in data:
        raise HTTPException(status_code = 400, detail="Patient already exists" )

    data[patient.id] = patient.model_dump(exclude=['id'])
    save_data(data)
    return JSONResponse(status_code = 201, content = {"message":"patient created successfully"})
