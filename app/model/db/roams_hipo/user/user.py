from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional


class BaseUserModel(BaseModel):
    dni: Optional[str] = Field(
        None, min_length=8, max_length=10, description="DNI del usuario"
    )
    email: Optional[EmailStr] = Field(None, description="Correo electrónico válido")
    name: Optional[str] = Field(
        None, min_length=1, max_length=100, description="Nombre del usuario"
    )

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


class UserInsertModel(BaseUserModel):
    dni: str = Field(..., min_length=8, max_length=10, description="DNI del usuario")
    email: EmailStr = Field(..., description="Correo electrónico válido")
    name: str = Field(
        ..., min_length=1, max_length=100, description="Nombre del usuario"
    )


class UserUpdateModel(BaseUserModel):
    pass


class UserDeleteModel(BaseUserModel):
    dni: str = Field(..., min_length=8, max_length=10, description="DNI del usuario")
