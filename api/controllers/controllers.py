
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import HTTPException
import models


def upload(request_body, file):
    try:
        patients = models.Patient.convert_csv_data_to_patients(file) if file else models.Patient.convert_request_data_to_patients(request_body)
        models.Patient.save_patients(patients)
        json_compatible_item_data = jsonable_encoder(patients)
        return JSONResponse(content=json_compatible_item_data)
    except:
        raise HTTPException(status_code=500, detail="Failed to upload")


def get_patient(id):
    patient = models.Patient.get_patient_by_id(id)
    json_compatible_item_data = jsonable_encoder(patient)
    return JSONResponse(content=json_compatible_item_data)
