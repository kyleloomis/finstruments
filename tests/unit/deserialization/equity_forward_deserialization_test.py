import unittest
from datetime import date

from finstruments.common.enum import Currency
from finstruments.instrument.common.cut import NysePMCut
from finstruments.instrument.common.exercise_style import EuropeanExerciseStyle
from finstruments.instrument.equity import CommonStock
from finstruments.instrument.equity import EquityForward
from tests.unit.deserialization.util import (
    assert_serialization,
    AdditionalEquity,
)


class TestEquityForwardDeserialization(unittest.TestCase):
    def test_base_serialization(self):
        expected = EquityForward(
            underlying=CommonStock(ticker="TEST"),
            exercise_type=EuropeanExerciseStyle(
                expiration_date=date(2022, 6, 1), cut=NysePMCut()
            ),
            strike_price=100,
            denomination_currency=Currency.USD,
            contract_size=100,
        )
        assert_serialization(expected, EquityForward)

    def test_equity_annotation_update(self):
        expected = EquityForward(
            underlying=AdditionalEquity(ticker="TEST"),
            exercise_type=EuropeanExerciseStyle(
                expiration_date=date(2022, 6, 1), cut=NysePMCut()
            ),
            strike_price=100,
            denomination_currency=Currency.USD,
            contract_size=100,
        )
        assert_serialization(expected, EquityForward)
        assert_serialization(expected.underlying, AdditionalEquity)
