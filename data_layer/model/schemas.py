from typing import Optional, List
from pydantic import BaseModel


class PydanticPatientDetails(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: Optional[str]


class PydanticPatientPhone(BaseModel):
    phone_number: str
    type: str


class PydanticPatient(BaseModel):
    phones: List[PydanticPatientPhone]
    details: Optional[PydanticPatientDetails]


class PydanticPatients(BaseModel):
    patients: List[PydanticPatient]

class PydanticPatientId(BaseModel):
    id: str