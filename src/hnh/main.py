from typing import Annotated
from fastapi import FastAPI, UploadFile
from transformers import pipeline

from hnh.predict import predict

from PIL import Image
import io

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

        model = pipeline("image-classification", model="julien-c/hotdog-not-hotdog")
        #model.save_pretrained("./saved_model")

        img = await file.read()
        img = Image.open(io.BytesIO(img))
        p = model(img)
        print(f"당신이 넣은 이미지는")
        print(f"{p[0]['score']*100:.2f}%의 확률로 {p[0]['label']}이며")
        print(f"{p[1]['score']*100:.2f}%의 확률로 {p[1]['label']}입니다.")


        return {
            "filename": file.filename,
            "predict": p[0]['label'] if p[0]['score']>p[1]['score'] else p[1]['label']
        }
