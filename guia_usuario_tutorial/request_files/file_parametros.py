from typing import Annotated
from fastapi import FastAPI, File, UploadFile


app = FastAPI()


# le o tamanho de um arquivo
@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


# exibe o nome do arquivo que foi carregado
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename, "content_type": file.content_type, "file": file.file}
