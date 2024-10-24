from abc import ABC
from typing import Optional, Union

from pydantic import Field

from finstruments.common.decorators import serializable_base_class
from finstruments.common.enum import Currency
from finstruments.instrument.abstract import BaseInstrument
from finstruments.instrument.common.exercise_style import BaseExerciseStyle
from finstruments.instrument.common.option.enum import BarrierType, DoubleBarrierType
from finstruments.instrument.common.option.payoff import BaseFixedStrikePayoff


@serializable_base_class
class VanillaOption(BaseInstrument, ABC):
    payoff: BaseFixedStrikePayoff
    exercise_type: BaseExerciseStyle
    denomination_currency: Currency
    agreed_discount_rate: Optional[str] = Field(default=None)
    code: str

    def __init__(self, **data):
        exercise_type: Union[dict, BaseExerciseStyle] = data.get("exercise_type")
        if isinstance(exercise_type, dict):
            data["pillar_date"] = exercise_type["expiration_date"]
        else:
            data["pillar_date"] = exercise_type.expiration_date
        super().__init__(**data)


@serializable_base_class
class BarrierOption(BaseInstrument, ABC):
    barrier_type: BarrierType
    barrier: float
    rebate: float
    payoff: BaseFixedStrikePayoff
    exercise_type: BaseExerciseStyle
    denomination_currency: Currency
    agreed_discount_rate: Optional[str] = Field(default=None)
    code: str

    def __init__(self, **data):
        exercise_type: Union[dict, BaseExerciseStyle] = data.get("exercise_type")
        if isinstance(exercise_type, dict):
            data["pillar_date"] = exercise_type["expiration_date"]
        else:
            data["pillar_date"] = exercise_type.expiration_date
        super().__init__(**data)


@serializable_base_class
class DoubleBarrierOption(BaseInstrument, ABC):
    barrier_type: DoubleBarrierType
    barrier_high: float
    barrier_low: float
    rebate: float
    payoff: BaseFixedStrikePayoff
    exercise_type: BaseExerciseStyle
    denomination_currency: Currency
    agreed_discount_rate: Optional[str] = Field(default=None)
    code: str

    def __init__(self, **data):
        exercise_type: Union[dict, BaseExerciseStyle] = data.get("exercise_type")
        if isinstance(exercise_type, dict):
            data["pillar_date"] = exercise_type["expiration_date"]
        else:
            data["pillar_date"] = exercise_type.expiration_date
        super().__init__(**data)
