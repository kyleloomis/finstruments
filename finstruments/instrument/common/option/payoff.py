from abc import ABC, abstractmethod

from finstruments.common.base import Base
from finstruments.common.decorators import serializable, serializable_base_class
from finstruments.instrument.common.option.enum import OptionType


@serializable_base_class
class BasePayoff(Base, ABC):
    @abstractmethod
    def compute_payoff(self, reference_level: float) -> float:
        """
        Compute payoff based on reference level.

        Args:
            reference_level (float): Spot price at expiration

        Returns:
            float: Payoff result
        """
        pass


@serializable_base_class
class BaseFixedStrikePayoff(BasePayoff, ABC):
    option_type: OptionType
    strike_price: float


@serializable
class VanillaPayoff(BaseFixedStrikePayoff):
    def compute_payoff(self, reference_level: float) -> float:
        """
        Compute payoff for vanilla call or put.

        Args:
            reference_level (float): Spot price at expiration

        Returns:
            float: Payoff result calculated using reference level and strike price
        """
        if self.option_type == OptionType.CALL:
            return (
                reference_level - self.strike_price
                if reference_level > self.strike_price
                else 0
            )
        elif self.option_type == OptionType.PUT:
            return (
                self.strike_price - reference_level
                if self.strike_price > reference_level
                else 0
            )


@serializable
class DigitalPayoff(BaseFixedStrikePayoff):
    cash_payout: float

    def compute_payoff(self, reference_level: float) -> float:
        """
        Compute payoff for digital call or put.

        Args:
            reference_level (float): Spot price at expiration

        Returns:
            float: Payoff result equivalent to cash_payout field
        """
        if self.option_type == OptionType.CALL:
            return self.cash_payout if reference_level > self.strike_price else 0
        elif self.option_type == OptionType.PUT:
            return self.cash_payout if self.strike_price > reference_level else 0
