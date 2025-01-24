from app.controller.service.request import Request

from app.controller.use_case.mortgage_sim.new_sim import (
    NewSim as NewSimUseCase,
)


class NewSim(Request):

    async def post(self, body):
        result_code, data = await NewSimUseCase(self.id_funtionality).xnew_sim(body)

        return await self.build_response_rest(result_code, data)

    async def get(self, body):
        result_code, data = await NewSimUseCase(self.id_funtionality).xnew_sim(body)

        return await self.build_response_rest(result_code, data)
