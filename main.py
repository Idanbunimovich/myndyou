from fastapi import FastAPI, Depends, UploadFile
import api.controllers.controllers as controllers
import data_layer.model.schemas as schemas
from typing import Union
import uvicorn

app = FastAPI()


@app.get("/patient")
async def get_patient(id: schemas.PydanticPatientId):
    controllers.get_patient(id)

@app.post("/patient")
async def upload(base: Union[schemas.PydanticPatients, None] = Depends(schemas.PydanticPatients),
                 file: Union[None, UploadFile] = None):
    controllers.upload(base, file)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)





