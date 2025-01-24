from fastapi.encoders import jsonable_encoder

from app.core.response.result import ResultAPI


class JSONResponseKeys:
    HEADER = "header"
    BODY = "body"
    RESULT = "result"


class JSONResponseAPI:

    def __init__(
        self,
        result=None,
        data=None,
    ):

        if result:
            self.result = result
        else:
            self.result = ResultAPI()

        if data is not None:
            self.body = data
