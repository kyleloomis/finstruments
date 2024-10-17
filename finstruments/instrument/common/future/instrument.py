from abc import ABC
from pydantic import Field
from typing import Optional, Union

from finstruments.common.decorators import serializable_base_class
from finstruments.common.enum import Currency
from finstruments.instrument.abstract import BaseInstrument
from finstruments.instrument.common.exercise_style import BaseExerciseStyle


@serializable_base_class
class VanillaFuture(BaseInstrument, ABC):
    underlying: BaseInstrument
    exercise_type: BaseExerciseStyle
    strike_price: float
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
