from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


def generate_html_reponse():
    html_content = """
        <html>
            <head>
                <title>Some HTML in here</title>
            </head>
            <body>
                <h1>Look ma! HTML!</h1>
            </body>
        </html>
        """
    return HTMLResponse(content=html_content, status_code=200)


# aparece na documentação pois estamos usando o response class
@app.get("/items/", response_class=HTMLResponse)
async def read_items():
    return generate_html_reponse()
