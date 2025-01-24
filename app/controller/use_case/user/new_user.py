from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import IntegrityError


from app.controller.use_case.use_case import UseCase
from app.controller.use_case.user._keys import UserKeys, UserResultCodes

from app.model.db.roams_hipo.user import UserInsertModel, UserDao


class NewUser(UseCase):
    async def xnew_user(self, body):
        user_model = self.validate_content(body, UserInsertModel)

        user = await UserDao().insert(user_model)

        if isinstance(user, IntegrityError):
            return (UserResultCodes.USER_ALREADY_EXISTS, True), None

        if isinstance(user, Exception):
            return (UserResultCodes.USER_FAIL, True), None

        return (UserResultCodes.USER_OK, False), None
