import unittest
from datetime import date

from finstruments.common.date import create_dates_between
from finstruments.instrument.common.cut import NysePMCut
from finstruments.instrument.common.exercise_style import (
    EuropeanExerciseStyle,
    AmericanExerciseStyle,
    BermudanExerciseStyle,
)


class ExerciseStyleTest(unittest.TestCase):
    def test_european_exercise_style_exercise(self):
        style = EuropeanExerciseStyle(expiration_date=date(2022, 1, 1), cut=NysePMCut())
        self.assertFalse(style.can_exercise(date(2021, 1, 1)))
        self.assertFalse(style.can_exercise(date(2022, 1, 2)))
        self.assertTrue(style.can_exercise(date(2022, 1, 1)))

    def test_european_exercise_style_schedule(self):
        style = EuropeanExerciseStyle(expiration_date=date(2022, 1, 1), cut=NysePMCut())
        self.assertListEqual(style.get_schedule(), [date(2022, 1, 1)])

    def test_american_exercise_style_exercise(self):
        style = AmericanExerciseStyle(
            minimum_exercise_date=date(2021, 1, 1),
            expiration_date=date(2022, 1, 1),
            cut=NysePMCut(),
        )
        self.assertFalse(style.can_exercise(date(2022, 1, 2)))
        self.assertTrue(style.can_exercise(date(2021, 6, 1)))
        self.assertTrue(style.can_exercise(date(2022, 1, 1)))

    def test_american_exercise_style_schedule(self):
        style = AmericanExerciseStyle(
            minimum_exercise_date=date(2021, 1, 1),
            expiration_date=date(2022, 1, 1),
            cut=NysePMCut(),
        )
        self.assertListEqual(
            style.get_schedule(),
            create_dates_between(date(2021, 1, 1), date(2022, 1, 1)),
        )

    def test_bermudan_exercise_style_exercise(self):
        style = BermudanExerciseStyle(
            early_exercise_dates=[date(2021, 1, 1), date(2021, 7, 1)],
            expiration_date=date(2022, 1, 1),
            cut=NysePMCut(),
        )
        self.assertFalse(style.can_exercise(date(2022, 1, 2)))
        self.assertFalse(style.can_exercise(date(2021, 7, 2)))
        self.assertTrue(style.can_exercise(date(2021, 1, 1)))
        self.assertTrue(style.can_exercise(date(2021, 7, 1)))
        self.assertTrue(style.can_exercise(date(2022, 1, 1)))

    def test_bermudan_exercise_style_schedule(self):
        style = BermudanExerciseStyle(
            early_exercise_dates=[date(2021, 1, 1), date(2021, 7, 1)],
            expiration_date=date(2022, 1, 1),
            cut=NysePMCut(),
        )
        self.assertListEqual(
            style.get_schedule(), [date(2021, 1, 1), date(2021, 7, 1), date(2022, 1, 1)]
        )
