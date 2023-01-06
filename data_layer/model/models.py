from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
import enum
from sqlalchemy.orm import relationship
from data_layer.lib.db import Base
from sqlalchemy.sql import func

class PhoneType(enum.Enum):
    home = 'home'
    mobile = 'mobile'


class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(Integer)
    date_created = Column(DateTime(timezone=True), default=func.now())


class PatientDetails(Base):
    __tablename__ = "patients_details"
    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    first_name = Column(String(16))
    last_name = Column(String(16))
    date_of_birth = Column(DateTime, nullable=True)
    patients = relationship("Patient", back_ref="patients")


class PatientPhone(Base):
    __tablename__ = "patients_phones"
    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    phone_number = Column(String(30))
    type = Column(Enum(PhoneType))
    patients = relationship("Patient", back_ref="patients")

