from customParser import parse_csv, parse_json
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import HTTPException
import models


def upload(patients, file):
    try:
        patients = parse_csv(file) if file else parse_json(patients)
        models.Patient.save_patients(patients)
        json_compatible_item_data = jsonable_encoder(patients)
        return JSONResponse(content=json_compatible_item_data)
    except:
        raise HTTPException(status_code=500, detail="Failed to upload")


def get_patient(id):
    patient = models.Patient.get_patient_by_id(id)
    json_compatible_item_data = jsonable_encoder(patient)
    return JSONResponse(content=json_compatible_item_data)
