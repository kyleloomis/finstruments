from abc import ABC, abstractmethod
from datetime import date, datetime, time

from pydantic import validator, Field
from pytz import timezone
from pytz.tzinfo import DstTzInfo

from finstruments.common.base import Base
from finstruments.common.date import date_to_datetime
from finstruments.common.decorators import serializable, serializable_base_class


@serializable_base_class
class BaseObservationCut(Base, ABC):
    class Config(Base.Config):
        arbitrary_types_allowed = True

    timezone: DstTzInfo

    @validator("timezone", pre=True, allow_reuse=True)
    def parse_timezone(cls, value):
        return timezone(value)

    @abstractmethod
    def get_observation_datetime(self, as_of_date: date) -> datetime:
        pass


@serializable
class NyseAMCut(BaseObservationCut):
    timezone: DstTzInfo = Field(default=timezone("US/Eastern"), init=False)

    def get_observation_datetime(self, as_of_date: date) -> datetime:
        dt = date_to_datetime(as_of_date, time(9, 30, 0))
        return self.timezone.localize(dt)


@serializable
class NysePMCut(BaseObservationCut):
    timezone: DstTzInfo = Field(default=timezone("US/Eastern"), init=False)

    def get_observation_datetime(self, as_of_date: date) -> datetime:
        dt = date_to_datetime(as_of_date, time(16, 0, 0))
        return self.timezone.localize(dt)
