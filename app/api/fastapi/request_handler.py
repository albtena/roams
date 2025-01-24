from fastapi import HTTPException

from app.core.response.response import JSONResponseAPI, JSONResponseKeys

from app.controller.service.request import RequestKeys
from app.util import object as Obj


#########################################
################## API ##################
#########################################

# Paths hardcodeadas para este ejemplo.
# Aqui vendria un modulo de autorizacion basado en path registradas, permisos y gestion de usuarios
# Se implementaria el decorador @auth 
available_paths = [
    "user/new_user",
    "user/get_user",
    "user/update_user",
    "mortgage_sim/new_sim"
]

#@auth
# Atiende las funcionalidades por método POST
async def funtionality_POST(path, content):
    if path not in available_paths:
        raise HTTPException(status_code=404, detail="Not Found")

    request_func = _get_request(path)

    if hasattr(request_func, RequestKeys.POST):
        result, data = await getattr(request_func, RequestKeys.POST)(body=content)

        return JSONResponseAPI(result=result, data=data)

    else:
        raise HTTPException(status_code=501, detail="Not Implemented POST funtionality")


# Atiende las funcionalidades por método GET
# async def funtionality_GET(path, content=None):
#     if path not in available_paths:
#         raise HTTPException(status_code=404, detail="Not Found")
    
#     request_func = _get_request(path)

#     if hasattr(request_func, RequestKeys.GET):
#         header, result, data = await getattr(request_func, RequestKeys.GET)(
#             content=content,
#         )

#         return JSONResponseAPI(body_header=header, result=result, data=data)

#     else:
#         raise HTTPException(status_code=501, detail="Not Implemented GET funtionality")


def _get_request(path):
    segments = path.split("/")

    return Obj.instance_request(segments=segments, type=Obj.JSON_PATH, params=None)
