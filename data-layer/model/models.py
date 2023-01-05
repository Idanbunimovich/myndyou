from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
import enum
from sqlalchemy.orm import relationship
from db import Base, session_factory
from sqlalchemy.sql import func
import datetime
from customParser import parse_csv, parse_json


class PhoneType(enum.Enum):
    home = 'home'
    mobile = 'mobile'


class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(Integer)
    date_created = Column(DateTime(timezone=True), default=func.now())

    @staticmethod
    def get_patient_by_id(input_id):
        session = session_factory()
        query_result = session.query(Patient, PatientPhone, PatientDetails) \
            .filter(Patient.id == input_id) \
            .filter(Patient.id == PatientPhone.patient_id) \
            .filter(Patient.id == PatientDetails.patient_id) \
            .all()
        session.close()
        result = {'phones': []}
        for (patient, patient_details, phone) in query_result:
            if not hasattr(result, 'patient'):
                result['patient'] = patient
                result['patient_details'] = patient_details
            result['phones'].append(phone)
        return result

    @staticmethod
    def save_patients(patients):
        session = session_factory()
        for patient in patients:
            new_patient = Patient(status=1)
            new_patient.patient_phones = []

            for phone in patient["phones"]:
                new_patient.patient_phones.append(PatientPhone(phone_number=phone["phone_number"], type=phone["type"]))
            new_patient.patient_details.append(PatientDetails(first_name=patient["first_name"],
                                                                    last_name=patient["last_name"],
                                                                    date_of_birth=datetime.datetime.strptime(patient["date_of_birth"], '%Y-%d-%m'))
            session.add(new_patient)
        session.commit()
        return patients

    @staticmethod
    def convert_request_data_to_patients(base):
        result = []
        for patient in base.patients:
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




class PatientDetails(Base):
    __tablename__ = "patients_details"
    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    first_name = Column(String(16))
    last_name = Column(String(16))
    date_of_birth = Column(DateTime, nullable=True)
    patients = relationship("Patient")


class PatientPhone(Base):
    __tablename__ = "patients_phones"
    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    phone_number = Column(String(30))
    type = Column(Enum(PhoneType))
    patients = relationship("Patient")


Patient.patient_details = relationship("PatientDetails")
Patient.patient_phones = relationship("PatientPhone")
