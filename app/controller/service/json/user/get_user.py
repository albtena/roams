from app.controller.service.request import Request

from app.controller.use_case.user.get_user import (
    GetUser as GetUserUseCase,
)


class GetUser(Request):

    async def post(self, body):
        result_code, data = await GetUserUseCase(self.id_funtionality).xget_user(body)

        return await self.build_response_rest(result_code, data)

    async def get(self, body):
        result_code, data = await GetUserUseCase(self.id_funtionality).xget_user(body)

        return await self.build_response_rest(result_code, data)
