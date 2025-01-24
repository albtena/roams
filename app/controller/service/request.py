from fastapi import HTTPException

from app.core.response.result import ResultAPI
from app.core.response.error import ResponseError


class RequestKeys:
    # Tipos de request
    POST = "post"
    GET = "get"


class Request:

    def __init__(self, id_funtionality=None, request=None):
        self.id_funtionality = id_funtionality
        self.request = request

    async def build_response_rest(self, result, data=None):
        if isinstance(result, Exception):
            ResponseError.return_not_available()

        return await self.build_response(result, data)

    async def build_response(self, result, data=None):
        if isinstance(result, ResultAPI):
            result_api = result
        elif isinstance(result, tuple):
            code, error = result
            result_api = ResultAPI(code=code, error=error)
        else:
            result_api = None

        return result_api, data

    async def post(self, user, header, body):
        raise HTTPException(status_code=501, detail="Not Implemented POST funtionality")

    async def get(self, user, header, body):
        raise HTTPException(status_code=501, detail="Not Implemented GET funtionality")
