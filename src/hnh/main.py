from typing import Annotated
from fastapi import FastAPI, UploadFile, Request
from transformers import pipeline
from PIL import Image
import io
#################################################
from fastapi.templating import Jinja2Templates
#################################################

from hnh.utils import get_max_score, get_max_score2

app = FastAPI()
html = Jinja2Templates(directory="public")

@app.get("/")
async def home(request: Request):
    import random
    hotdog = f"{__file__}/../../../public/hotdog.webp"
    dog = f"{__file__}/../../../public/hotdog.webp"
    image_url = random.choice([hotdog, dog])
    print(request.__dir__())

    return html.TemplateResponse("index.html",{"request":request, "image_url": image_url})

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    ftype, ext = file.content_type.split("/")

    if ftype!="image":
        return "잘못된 형식, 이미지 파일을 업로드해주세요"
    else:
        print(file.filename)
        #pred = predict()

        model = pipeline("image-classification", model="julien-c/hotdog-not-hotdog")
        #model.save_pretrained("./saved_model")

        img = await file.read()
        img = Image.open(io.BytesIO(img))
        p = model(img)

        print(get_max_score2(p))


        return {
            "filename": file.filename,
            "predict": get_max_score(p)
        }
