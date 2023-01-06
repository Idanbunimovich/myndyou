
from fastapi import HTTPException
from data_layer.model.patient import Patient


def upload(request_body, file):
    try:
        patients = Patient.convert_csv_data_to_patients(file) if file else Patient.convert_request_data_to_patients(request_body)
        return Patient.save_patients(patients)
    except:
        raise HTTPException(status_code=500, detail="Failed to upload")


def get_patient(id):
    try:
        patient = Patient.get_patient_by_id(id)
        if not patient:
            raise HTTPException(status_code=404, detail="Patient not found")
        return patient
    except:
        raise HTTPException(status_code=500, detail="Failed to get patient")
