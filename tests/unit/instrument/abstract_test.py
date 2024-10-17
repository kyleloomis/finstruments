import unittest
from datetime import date

from finstruments.common.enum import Currency
from finstruments.instrument.common.cut import NysePMCut
from finstruments.instrument.common.exercise_style import EuropeanExerciseStyle
from finstruments.instrument.common.option.enum import OptionType
from finstruments.instrument.common.option.payoff import VanillaPayoff
from finstruments.instrument.equity import EquityETF, EquityOption


class BaseInstrumentTest(unittest.TestCase):
    def test_base_instrument(self):
        etf: EquityETF = EquityETF(ticker="SPY")
        option: EquityOption = EquityOption(
            underlying=EquityETF(ticker="SPY"),
            payoff=VanillaPayoff(option_type=OptionType.CALL, strike_price=100),
            exercise_type=EuropeanExerciseStyle(
                expiration_date=date(2022, 5, 2), cut=NysePMCut()
            ),
            denomination_currency=Currency.USD,
            contract_size=100,
        )

        self.assertEqual(option.underlying_instrument, EquityETF(ticker="SPY"))
        self.assertEqual(option.underlying_instrument, option.underlying)
        # `.underlying_instrument` should return self
        self.assertEqual(etf.underlying_instrument, etf)
