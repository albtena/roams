from pydantic import BaseModel, Field, field_validator
from typing import Optional


class BaseMortgageSimModel(BaseModel):
    dni: Optional[str] = Field(
        None, min_length=8, max_length=10, description="DNI del usuario"
    )
    requested_capital: Optional[float] = Field(
        None, gt=0, description="Capital solicitado, debe ser mayor que 0"
    )
    tae: Optional[float] = Field(
        None, gt=0, le=100, description="TAE, debe estar entre 0 y 100"
    )
    amortization_period: Optional[float] = Field(
        None, gt=0, description="Periodo de amortización en años, debe ser mayor a 0"
    )
    monthly_payment: Optional[float] = Field(
        None, gt=0, description="Cuota mensual, debe ser mayor a 0"
    )
    total_amount: Optional[float] = Field(
        None, gt=0, description="Importe total a deber, debe ser mayor a 0"
    )
    id: Optional[int] = Field(None, ge=0, description="ID único del registro")

    @field_validator("dni")
    def validate_dni(cls, value):
        if value is None:
            return value  # Puede ser opcional
        valid_letters = "TRWAGMYFPDXBNJZSQVHLCKE"
        numbers = int(value[:-1])
        letter = value[-1]
        if valid_letters[numbers % 23] != letter:
            raise ValueError("DNI letter not valid.")
        return value

    class Config:
        extra = "ignore"


class MortgageSimInsertModel(BaseMortgageSimModel):
    dni: Optional[str] = Field(..., min_length=8, max_length=10)
    requested_capital: float = Field(
        ..., gt=0, description="Capital solicitado, debe ser mayor que 0"
    )
    tae: float = Field(..., gt=0, le=100, description="TAE, debe estar entre 0 y 100")
    amortization_period: float = Field(
        None, gt=0, description="Periodo de amortización en años, debe ser mayor a 0"
    )
    monthly_payment: float = Field(
        ..., gt=0, description="Cuota mensual, debe ser mayor a 0"
    )
    total_amount: float = Field(
        ..., gt=0, description="Importe total a deber, debe ser mayor a 0"
    )


class MortgageSimInputModel(BaseMortgageSimModel):
    dni: str = Field(..., min_length=8, max_length=10)
    requested_capital: float = Field(
        ..., gt=0, description="Capital solicitado, debe ser mayor que 0"
    )
    tae: float = Field(..., gt=0, le=100, description="TAE, debe estar entre 0 y 100")
    amortization_period: float = Field(
        ..., gt=0, description="Periodo de amortización en años, debe ser mayor a 0"
    )


class MortgageSimUpdateModel(BaseMortgageSimModel):
    id: int = Field(..., ge=0, description="ID único del registro")
    pass


class MortgageSimDeleteModel(BaseModel):
    id: int = Field(..., description="ID único del registro")
