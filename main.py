import sys
sys.path.insert(1, 'C:/Users/idan/PycharmProjects/nlp_dev/data-layer/lib')
sys.path.insert(2, 'C:/Users/idan/PycharmProjects/nlp_dev/data-layer/model')
sys.path.insert(3, 'C:/Users/idan/PycharmProjects/nlp_dev/api/controllers')
from fastapi import FastAPI, File, Depends, UploadFile
import controllers
import schemas
from typing import Union
import uvicorn

app = FastAPI()


@app.get("/patient")
async def get_patient(id):
    controllers.get_patient(id)

@app.post("/patient")
async def upload(base: Union[schemas.PydanticPatients, None] = Depends(schemas.PydanticPatients),
                 file: Union[None, UploadFile] = None):
    controllers.upload(base, file)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)





