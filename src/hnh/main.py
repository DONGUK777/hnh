from typing import Annotated
from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


#@app.post("/uploadfile/")
#async def create_upload_file(file: UploadFile):
#    return {"filename": file.filename}

@app.post("/predict/")
async def pred(name: str):
    food = ["hot", "dog", "hotdog"]
    if name in food:
       result  = 'HotDog'
       return result
    else:
        result = 'Not HotDog'
        return result
    

