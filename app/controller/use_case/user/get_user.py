from fastapi.encoders import jsonable_encoder

from app.core.response.error import ResponseError
from sqlalchemy.exc import IntegrityError

from app.controller.use_case.use_case import UseCase, UseCaseKeys
from app.controller.use_case.user._keys import UserKeys, UserResultCodes

from app.model.db.roams_hipo.user import BaseUserModel, UserDao
from app.model.db.roams_hipo.mortgage_sim import BaseMortgageSimModel, MortgageSimDao


from app.util import date as Dt


class GetUser(UseCase):
    async def xget_user(self, body):
        user_model = self.validate_content(body, BaseUserModel)

        user = await UserDao().get_user(user_model)

        if not user:
            return (UserResultCodes.USER_NOT_EXISTS, True), None

        if isinstance(user, Exception):
            return (UserResultCodes.USER_FAIL, True), None

        mortgage_model = BaseMortgageSimModel(dni=user.dni)

        mortgage_sims = await MortgageSimDao().get_mortgage_sims(mortgage_model)

        if isinstance(mortgage_sims, Exception):
            return (UserResultCodes.USER_FAIL, True), None

        data = {
            "user": jsonable_encoder(user),
            "mortgage_sim_list": (
                jsonable_encoder(mortgage_sims) if mortgage_sims else []
            ),
        }

        return (UserResultCodes.USER_OK, False), data
