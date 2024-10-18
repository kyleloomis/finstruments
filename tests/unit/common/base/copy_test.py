import unittest
from datetime import date
from finstruments.portfolio import Position

from finstruments.common.enum import Currency
from finstruments.instrument.common.cut import NysePMCut
from finstruments.instrument.common.exercise_style import EuropeanExerciseStyle
from finstruments.instrument.common.option.enum import OptionType
from finstruments.instrument.common.option.payoff import VanillaPayoff
from finstruments.instrument.equity import EquityOption, CommonStock


class TestCopy(unittest.TestCase):
    def setUp(self) -> None:
        self.position = Position(
            instrument=EquityOption(
                underlying=CommonStock(ticker="TEST"),
                payoff=VanillaPayoff(option_type=OptionType.CALL, strike_price=100),
                exercise_type=EuropeanExerciseStyle(
                    expiration_date=date(2022, 6, 1), cut=NysePMCut()
                ),
                denomination_currency=Currency.USD,
                contract_size=100,
            ),
            size=100,
        )

    def test_copy(self):
        copy = self.position.copy()
        self.assertEqual(self.position, copy)

    def test_copy_with_ignored_fields(self):
        copy = self.position.copy(ignored_fields=["id"])
        self.assertNotEqual(self.position.id, copy.id)

    def test_copy_with_ignored_fields_and_nested_alterations(self):
        copy = self.position.copy(
            ignored_fields=["instrument.agreed_discount_rate"],
            **{"instrument.underlying": CommonStock(ticker="TEST2")},
        )
        self.assertEqual(copy.instrument.agreed_discount_rate, None)
        self.assertEqual(self.position.id, copy.id)
        self.assertEqual(self.position.size, copy.size)
        self.assertNotEqual(
            self.position.instrument.underlying, copy.instrument.underlying
        )

    def test_copy_with_nested_alterations(self):
        copy = self.position.copy(
            **{"instrument.underlying": CommonStock(ticker="TEST2")}
        )
        self.assertEqual(self.position.id, copy.id)
        self.assertEqual(self.position.size, copy.size)
        self.assertNotEqual(
            self.position.instrument.underlying, copy.instrument.underlying
        )

    def test_copy_with_alterations(self):
        copy = self.position.copy(size=10)
        self.assertEqual(self.position.id, copy.id)
        self.assertEqual(self.position.instrument, copy.instrument)
        self.assertNotEqual(self.position.size, copy.size)
