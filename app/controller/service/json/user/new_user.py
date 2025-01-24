from app.controller.service.request import Request

from app.controller.use_case.user.new_user import (
    NewUser as NewUserUseCase,
)


class NewUser(Request):

    async def post(self, body):
        result_code, data = await NewUserUseCase(self.id_funtionality).xnew_user(body)

        return await self.build_response_rest(result_code, data)

    async def get(self, body):
        result_code, data = await NewUserUseCase(self.id_funtionality).xnew_user(body)

        return await self.build_response_rest(result_code, data)
