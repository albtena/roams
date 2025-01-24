import os

from typing import List, Optional
from urllib.parse import parse_qs
from fastapi import Depends, FastAPI, Request, Query

from app.api.fastapi import request_handler as RequestHandler

if int(os.getenv("PRODUCTION")):
    print(" +++ Production enviroment loaded +++ ")
    app = FastAPI(docs_url=None, redoc_url=None)
else:
    print(" +++ Developer enviroment loaded +++ ")
    app = FastAPI()


@app.post("/{path:path}")
async def handle_post(
    request: Request,
    path: str,
    body: dict = {},
):
    # Llama a la función que manejará la solicitud con los segmentos dinámicos
    return await RequestHandler.funtionality_POST(
        path=path,
        content=body,
    )


