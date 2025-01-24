from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import IntegrityError
from pydantic import ValidationError

from app.controller.use_case.use_case import UseCase
from app.controller.use_case.mortgage_sim._keys import MortgageKeys, MortgageResultCodes

from app.model.db.roams_hipo.mortgage_sim import (
    MortgageSimInputModel,
    MortgageSimInsertModel,
    MortgageSimDao,
)


class NewSim(UseCase):
    async def xnew_sim(self, body):

        mortgage_model = self.validate_content(body, MortgageSimInputModel)

        tae_per = (mortgage_model.tae / 100) / 12

        monthly_payment = (
            mortgage_model.requested_capital
            * tae_per
            / (1 - (1 + tae_per) ** (-mortgage_model.amortization_period))
        )

        monthly_payment = round(monthly_payment, 2)

        total_amount = monthly_payment * mortgage_model.amortization_period

        total_amount = round(total_amount, 2)

        mortgage_model = MortgageSimInsertModel(
            dni=mortgage_model.dni,
            requested_capital=mortgage_model.requested_capital,
            tae=mortgage_model.tae,
            amortization_period=mortgage_model.amortization_period,
            monthly_payment=monthly_payment,
            total_amount=total_amount,
        )

        mortgage = await MortgageSimDao().insert(mortgage_model)

        data = jsonable_encoder(mortgage)

        data = self.clean_data(
            data, list_=[MortgageKeys.MONTHLY_PAYMENT, MortgageKeys.TOTAL_AMOUNT]
        )

        if isinstance(mortgage, Exception):
            return (MortgageResultCodes.MORTGAGE_FAIL, True), None

        return (MortgageResultCodes.MORTGAGE_OK, False), data
