import unittest
from datetime import date

from finstruments.common.enum import Currency
from finstruments.instrument.common.cut import NysePMCut
from finstruments.instrument.common.exercise_style import EuropeanExerciseStyle
from finstruments.instrument.common.option.enum import OptionType
from finstruments.instrument.common.option.payoff import VanillaPayoff
from finstruments.instrument.equity import EquityOption, CommonStock
from finstruments.portfolio import Position


class TestHash(unittest.TestCase):
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

    def test_hash(self):
        original_hash = hash(self.position)
        copy_hash = hash(self.position.copy())
        copy_hash_with_changes = hash(self.position.copy(ignored_fields=["id"]))

        self.assertEqual(original_hash, copy_hash)
        self.assertNotEqual(original_hash, copy_hash_with_changes)
        self.assertNotEqual(copy_hash, copy_hash_with_changes)

    def test_to_set(self):
        position_list = [self.position for _ in range(10)]
        position_set = set(position_list)
        self.assertEqual(len(position_set), 1)
