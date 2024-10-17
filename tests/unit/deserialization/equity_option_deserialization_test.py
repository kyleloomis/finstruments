import unittest
from datetime import date

from finstruments.common.enum import Currency
from finstruments.instrument.common.cut import NysePMCut
from finstruments.instrument.common.exercise_style import (
    EuropeanExerciseStyle,
    BermudanExerciseStyle,
)
from finstruments.instrument.common.option.enum import OptionType
from finstruments.instrument.common.option.payoff import VanillaPayoff, DigitalPayoff
from finstruments.instrument.equity import CommonStock, EquityIndex
from finstruments.instrument.equity import EquityOption
from finstruments.instrument.equity.enum import EquityIndexType
from tests.unit.deserialization.util import (
    assert_serialization,
    AdditionalEquity,
    AdditionalPayoff,
    AdditionalExerciseStyle,
)


class TestEquityOptionDeserialization(unittest.TestCase):
    def test_base_serialization(self):
        expected = EquityOption(
            underlying=CommonStock(ticker="TEST"),
            payoff=VanillaPayoff(option_type=OptionType.CALL, strike_price=100),
            exercise_type=EuropeanExerciseStyle(
                expiration_date=date(2022, 6, 1), cut=NysePMCut()
            ),
            denomination_currency=Currency.USD,
            contract_size=100,
        )

        expected_two = EquityOption(
            underlying=EquityIndex(
                ticker="TEST", index_type=EquityIndexType.TOTAL_RETURN
            ),
            payoff=DigitalPayoff(
                option_type=OptionType.CALL, strike_price=100, cash_payout=20
            ),
            exercise_type=BermudanExerciseStyle(
                expiration_date=date(2022, 6, 1),
                early_exercise_dates=[date(2022, 1, 1), date(2022, 3, 1)],
                cut=NysePMCut(),
            ),
            denomination_currency=Currency.USD,
            contract_size=100,
        )

        assert_serialization(expected, EquityOption)
        assert_serialization(expected_two, EquityOption)

    def test_equity_annotation_update(self):
        expected = EquityOption(
            underlying=AdditionalEquity(ticker="TEST"),
            payoff=VanillaPayoff(option_type=OptionType.CALL, strike_price=100),
            exercise_type=EuropeanExerciseStyle(
                expiration_date=date(2022, 6, 1), cut=NysePMCut()
            ),
            denomination_currency=Currency.USD,
            contract_size=100,
        )
        assert_serialization(expected, EquityOption)
        assert_serialization(expected.underlying, AdditionalEquity)

    def test_fixed_strike_payoff_annotation_update(self):
        expected = EquityOption(
            underlying=CommonStock(ticker="TEST"),
            payoff=AdditionalPayoff(option_type=OptionType.CALL, strike_price=100),
            exercise_type=EuropeanExerciseStyle(
                expiration_date=date(2022, 6, 1), cut=NysePMCut()
            ),
            denomination_currency=Currency.USD,
            contract_size=100,
        )
        assert_serialization(expected, EquityOption)

    def test_exercise_type_annotation_update(self):
        expected = EquityOption(
            underlying=CommonStock(ticker="TEST"),
            payoff=VanillaPayoff(option_type=OptionType.CALL, strike_price=100),
            exercise_type=AdditionalExerciseStyle(
                expiration_date=date(2022, 6, 1), cut=NysePMCut()
            ),
            denomination_currency=Currency.USD,
            contract_size=100,
        )
        assert_serialization(expected, EquityOption)
