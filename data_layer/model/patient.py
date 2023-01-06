import base
import models
import datetime
from data_layer.lib.customParser import parse_csv

class Patient(base):
    def __init__(self, model):
        super().__init__(model)

    def insert(self, patients):
        return super(Patient, self).insert(Patient.prepare_patients_for_save(patients))

    def get_patient_by_id(self, id):
        return self.get(id, [models.Patient.id == id])

    @staticmethod
    def prepare_patients_for_save(patients):
        result = []
        for patient in patients:
            new_patient = models.Patient(status=1)
            new_patient.patient_phones = []
            for phone in patient["phones"]:
                new_patient.patient_phones.append(models.PatientPhone(phone_number=phone["phone_number"], type=phone["type"]))
            new_patient.patient_details.append(models.PatientDetails(first_name=patient["first_name"],
                                                                     last_name=patient["last_name"],
                                                                     date_of_birth=datetime.datetime(datetime.datetime.strptime(patient["date_of_birth"], '%Y-%d-%m'))))
            result.append(new_patient)
        return result

    #
    @staticmethod
    def convert_request_data_to_patients(req):
        result = []
        for patient in req.patients:
            dict = {}
            dict['phones'] = []
            dict['first_name'] = patient.details.first_name
            dict['last_name'] = patient.details.last_name
            dict['date_of_birth'] = patient.details.date_of_birth
            for phone in patient.phones:
                dict['phones'].append({'type': phone.type, 'phone_number': phone.phone_number})
            result.append(dict)
        return result

    @staticmethod
    def convert_csv_data_to_patients(file):
        dict = parse_csv(file)
        dict['phones'] = [{'phone_number': dict['phone'], 'type': dict['type']}]
        return dict


