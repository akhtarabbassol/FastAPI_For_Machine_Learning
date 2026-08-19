from fastapi import FastAPI,Path, HTTPException
import json
app = FastAPI()
def load_data():
    with open("patients.json", 'r') as f:
        data = json.load(f)
    return data
data = load_data()
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