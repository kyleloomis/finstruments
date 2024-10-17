from abc import ABC
from datetime import date
from pydantic import Field
from typing import Optional

from finstruments.common.base import Base
from finstruments.common.decorators import serializable_base_class
from finstruments.common.enum import Currency


@serializable_base_class
class BaseInstrument(Base, ABC):
    """
    Base instrument data class to be inherited from all instrument subclasses. Contains core fields that are applicable
    to all instruments.
    """

    agreed_discount_rate: Optional[str] = Field(default=None)
    pillar_date: Optional[date] = Field(default=None)
    denomination_currency: Optional[Currency] = Field(default=None)
    code: str
    descriptor: str

    @property
    def underlying_instrument(self) -> "BaseInstrument":
        """
        Get and return BaseInstrument in "underlying" field if exists, else self.

        Returns:
            BaseInstrument: BaseInstrument in "underlying" field if exists, else self
        """
        return getattr(self, "underlying", None) or self
