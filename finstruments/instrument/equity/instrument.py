from abc import ABC
from datetime import date
from typing import Optional

from pydantic import Field

from finstruments.common.decorators import serializable, serializable_base_class
from finstruments.common.enum import Currency
from finstruments.instrument.abstract import BaseInstrument
from finstruments.instrument.common.exercise_style import (
    EuropeanExerciseStyle,
    BaseExerciseStyle,
)
from finstruments.instrument.common.forward import VanillaForward
from finstruments.instrument.common.future import VanillaFuture
from finstruments.instrument.common.option import VanillaOption
from finstruments.instrument.common.option.payoff import BaseFixedStrikePayoff
from finstruments.instrument.equity.enum import EquityIndexType


@serializable_base_class
class BaseEquity(BaseInstrument, ABC):
    """
    Equity base class.
    """

    ticker: str
    agreed_discount_rate: Optional[str] = Field(init=False, default=None)
    pillar_date: Optional[date] = Field(init=False, default=None)
    denomination_currency: Optional[Currency] = Field(default=None)
    code: str


@serializable
class EquityIndex(BaseEquity):
    """
    Equity index.
    """

    index_type: EquityIndexType
    code: str = Field(init=False, default="EQUITY_INDEX")


@serializable
class EquityETF(BaseEquity):
    """
    Equity ETF.
    """

    code: str = Field(init=False, default="EQUITY_ETF")


@serializable
class CommonStock(BaseEquity):
    """
    Common stock.
    """

    code: str = Field(init=False, default="COMMON_STOCK")


@serializable
class EquityForward(VanillaForward):
    underlying: BaseEquity
    exercise_type: EuropeanExerciseStyle
    strike_price: float
    contract_size: float
    denomination_currency: Currency
    agreed_discount_rate: Optional[str] = Field(default=None)
    code: str = Field(init=False, default="EQUITY_FORWARD")


@serializable
class EquityFuture(VanillaFuture):
    underlying: BaseEquity
    exercise_type: EuropeanExerciseStyle
    strike_price: float
    contract_size: float
    denomination_currency: Currency
    agreed_discount_rate: Optional[str] = Field(default=None)
    code: str = Field(init=False, default="EQUITY_FUTURE")


@serializable
class EquityOption(VanillaOption):
    underlying: BaseEquity
    payoff: BaseFixedStrikePayoff
    exercise_type: BaseExerciseStyle
    contract_size: float
    denomination_currency: Currency
    agreed_discount_rate: Optional[str] = Field(default=None)
    code: str = Field(init=False, default="EQUITY_OPTION")
