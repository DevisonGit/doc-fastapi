from typing import Annotated
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse


app = FastAPI()


# recebe uma lista de arquivos e exibe seus tamanhos
@app.post("/files/")
async def create_files(files: Annotated[list[bytes], File(description="teste")]):
    return {"files": [len(file) for file in files]}


# espera um lista de arquivos e exibe seus nomes
@app.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile]):
    return {"filesnames": [file.filename for file in files]}


# gera uma pagina HTML que permite selecionar arquivos e chama files ou uploadfiles
@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)
