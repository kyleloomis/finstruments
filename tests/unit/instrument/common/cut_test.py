import unittest
from datetime import date, time

from finstruments.common.date import datetime_to_timestamp, date_to_datetime
from finstruments.instrument.common.cut import NyseAMCut, NysePMCut


class ExerciseStyleCutTest(unittest.TestCase):
    def test_nyse_am_cut(self):
        cut = NyseAMCut()
        d = date(2020, 1, 1)
        cut_dt = cut.get_observation_datetime(d)
        dt = date_to_datetime(d, time(14, 30, 0))

        self.assertEqual(datetime_to_timestamp(cut_dt), datetime_to_timestamp(dt))

    def test_nyse_pm_cut(self):
        cut = NysePMCut()
        d = date(2020, 1, 1)
        cut_dt = cut.get_observation_datetime(d)
        dt = date_to_datetime(d, time(21, 0, 0))

        self.assertEqual(datetime_to_timestamp(cut_dt), datetime_to_timestamp(dt))
