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
    hotdog = f"https://github.com/Mingk42/mingk42-hnh/blob/v0.3.1/html/public/hotdog.png?raw=true"
    hotdog_no = f"https://github.com/Mingk42/mingk42-hnh/blob/v0.3.1/html/public/hotdog_no.png?raw=true"
    image_url = random.choice([hotdog, hotdog_no])

    return html.TemplateResponse("index.html",{"request":request, "image_url": image_url})

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile, request: Request):
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

        pred = get_max_score(p)

        import random
        img_url = {
            "hot dog" : f"https://github.com/Mingk42/mingk42-hnh/blob/v0.3.1/html/public/hotdog.png?raw=true",
            "not hot dog" : f"https://github.com/Mingk42/mingk42-hnh/blob/v0.3.1/html/public/hotdog_no.png?raw=true"
        }
        #return html.TemplateResponse("index.html",{"request":request, "image_url": img_url[pred], "pred":pred} )
        #return html.TemplateResponse("index.html",{"request":request, "image_url": img)

        return {
            "filename": file.filename,
            "predict": get_max_score(p),
            "label":pred,
            "image_url": img_url[pred]
        }

#         return {
#             "filename": file.filename,
#             "predict": get_max_score(p)
#         }