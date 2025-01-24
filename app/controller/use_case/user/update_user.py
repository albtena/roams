from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import IntegrityError


from app.controller.use_case.use_case import UseCase
from app.controller.use_case.user._keys import UserKeys, UserResultCodes

from app.model.db.roams_hipo.user import UserUpdateModel, UserDao


class UpdateUser(UseCase):
    async def xupdate_user(self, body):
        user_model = self.validate_content(body, UserUpdateModel)

        user = await UserDao().update(user_model)

        if isinstance(user, Exception):
            return (UserResultCodes.USER_FAIL, True), None

        return (UserResultCodes.USER_OK, False), None
