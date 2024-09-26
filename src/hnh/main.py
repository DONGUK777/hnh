from typing import Annotated
from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.get("/files/")
def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}

@app.get("/predict/")
def pred(name: str):
    food = ["hot", "dog", "hotdog"]
    if name in food:
       result  = 'HotDog'
       return result
    else:
        result = 'Not HotDog'
        return result
    

