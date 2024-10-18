from abc import ABC
from datetime import date
from typing import Optional

from pydantic import Field

from finstruments.common.decorators import serializable, serializable_base_class
from finstruments.common.enum import Currency
from finstruments.instrument.abstract import BaseInstrument
from finstruments.instrument.common.enum import SettlementType
from finstruments.instrument.common.exercise_style import (
    EuropeanExerciseStyle,
    BaseExerciseStyle,
)
from finstruments.instrument.common.forward import VanillaForward
from finstruments.instrument.common.future import VanillaFuture
from finstruments.instrument.common.option import VanillaOption
from finstruments.instrument.common.option.payoff import BaseFixedStrikePayoff


@serializable_base_class
class BaseCommodity(BaseInstrument, ABC):
    """
    Commodity base class.
    """

    name: str
    agreed_discount_rate: Optional[str] = Field(init=False, default=None)
    pillar_date: Optional[date] = Field(init=False, default=None)
    denomination_currency: Optional[Currency] = Field(default=None)
    code: str


@serializable
class CommodityIndex(BaseCommodity):
    """
    Commodity index.
    """

    code: str = Field(init=False, default="COMMODITY_INDEX")


@serializable
class Commodity(BaseCommodity):  # TODO rename
    """
    Commodity.
    """

    settlement_type: SettlementType
    code: str = Field(init=False, default="COMMODITY")


@serializable
class CommodityForward(VanillaForward):
    underlying: BaseCommodity
    exercise_type: EuropeanExerciseStyle
    strike_price: float
    contract_size: float
    unit: str
    denomination_currency: Currency
    agreed_discount_rate: Optional[str] = Field(default=None)
    code: str = Field(init=False, default="COMMODITY_FORWARD")


@serializable
class CommodityFuture(VanillaFuture):
    underlying: BaseCommodity
    exercise_type: EuropeanExerciseStyle
    strike_price: float
    contract_size: float
    unit: str
    denomination_currency: Currency
    agreed_discount_rate: Optional[str] = Field(default=None)
    code: str = Field(init=False, default="COMMODITY_FUTURE")


@serializable
class CommodityOption(VanillaOption):
    underlying: BaseCommodity
    payoff: BaseFixedStrikePayoff
    exercise_type: BaseExerciseStyle
    contract_size: float
    unit: str
    denomination_currency: Currency
    agreed_discount_rate: Optional[str] = Field(default=None)
    code: str = Field(init=False, default="COMMODITY_OPTION")


@serializable
class CommodityFutureOption(VanillaOption):
    underlying: CommodityFuture
    payoff: BaseFixedStrikePayoff
    exercise_type: BaseExerciseStyle
    contract_size: float
    unit: str
    denomination_currency: Currency
    agreed_discount_rate: Optional[str] = Field(default=None)
    code: str = Field(init=False, default="COMMODITY_FUTURE_OPTION")
