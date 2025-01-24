from typing import List, Optional

from sqlalchemy import Column, ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, Text
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy.orm.base import Mapped

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    __table_args__ = (
        PrimaryKeyConstraint('dni', name='user_PK'),
    )

    dni = mapped_column(Text)
    email = mapped_column(Text)
    name = mapped_column(Text)

    mortgage_sim: Mapped[List['MortgageSim']] = relationship('MortgageSim', uselist=True, back_populates='user')


class MortgageSim(Base):
    __tablename__ = 'mortgage_sim'
    __table_args__ = (
        ForeignKeyConstraint(['dni'], ['user.dni'], ondelete='CASCADE', onupdate='CASCADE', name='mortgage_sim_FK'),
    )

    dni = mapped_column(Text)
    requested_capital = mapped_column(Numeric)
    tae = mapped_column(Numeric)
    amortization_period = mapped_column(Numeric)
    monthly_payment = mapped_column(Numeric)
    total_amount = mapped_column(Numeric)
    id = mapped_column(Integer, primary_key=True)

    user: Mapped[Optional['User']] = relationship('User', back_populates='mortgage_sim')
