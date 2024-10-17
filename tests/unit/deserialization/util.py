from datetime import date
from pydantic import Field
from typing import List

from finstruments.common.base import Base
from finstruments.common.decorators import serializable
from finstruments.instrument.common.exercise_style import BaseExerciseStyle
from finstruments.instrument.common.option.payoff import BaseFixedStrikePayoff
from finstruments.instrument.equity.instrument import BaseEquity


def assert_serialization(expected: Base, object_type):
    data = expected.request_dict()
    result = object_type(**data)
    assert expected == result


@serializable
class AdditionalEquity(BaseEquity):
    code: str = Field(init=False, default="ADDITIONAL_EQUITY")


@serializable
class AdditionalPayoff(BaseFixedStrikePayoff):
    def compute_payoff(self, reference_level: float) -> float:
        return 0.0


@serializable
class AdditionalExerciseStyle(BaseExerciseStyle):
    def can_exercise(self, as_of_date: date) -> bool:
        return True

    def get_schedule(self) -> List[date]:
        return []


@serializable
class AdditionalInstrument(BaseExerciseStyle):
    def can_exercise(self, as_of_date: date) -> bool:
        return True

    def get_schedule(self) -> List[date]:
        return []
