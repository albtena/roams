from app.controller.service.request import Request

from app.controller.use_case.user.update_user import (
    UpdateUser as UpdateUserUseCase,
)


class UpdateUser(Request):

    async def post(self, body):
        result_code, data = await UpdateUserUseCase(self.id_funtionality).xupdate_user(
            body
        )

        return await self.build_response_rest(result_code, data)

    async def get(self, body):
        result_code, data = await UpdateUserUseCase(self.id_funtionality).xupdate_user(
            body
        )

        return await self.build_response_rest(result_code, data)
