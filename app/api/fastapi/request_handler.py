from fastapi import HTTPException

from app.core.response.response import JSONResponseAPI, JSONResponseKeys

from app.controller.service.request import RequestKeys
from app.util import object as Obj


#########################################
################## API ##################
#########################################


# Atiende las funcionalidades por método POST
async def funtionality_POST(path, content):

    request_func = _get_request(path)

    if hasattr(request_func, RequestKeys.POST):
        result, data = await getattr(request_func, RequestKeys.POST)(body=content)

        return JSONResponseAPI(result=result, data=data)

    else:
        raise HTTPException(status_code=501, detail="Not Implemented POST funtionality")


# Atiende las funcionalidades por método GET
async def funtionality_GET(path, content=None):
    request_func = _get_request(path)

    if hasattr(request_func, RequestKeys.GET):
        header, result, data = await getattr(request_func, RequestKeys.GET)(
            content=content,
        )

        return JSONResponseAPI(body_header=header, result=result, data=data)

    else:
        raise HTTPException(status_code=501, detail="Not Implemented GET funtionality")


def _get_request(path):
    segments = path.split("/")

    return Obj.instance_request(segments=segments, type=Obj.JSON_PATH, params=None)
