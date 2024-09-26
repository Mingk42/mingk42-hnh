from typing import Annotated
from fastapi import FastAPI, UploadFile

from hnh.predict import predict

app = FastAPI()


@app.get("/")
def read_root():

    return {
        "Conn" : "ok",
    }

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    ftype, ext = file.content_type.split("/")

    if ftype!="image":
        return "잘못된 형식, 이미지 파일을 업로드해주세요"
    else:
        print(file.filename)
        pred = predict()

        return {
            "filename": file.filename,
            "predict": pred
        }
