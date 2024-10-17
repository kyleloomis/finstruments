import unittest
from datetime import date, datetime
from pytz import timezone

from finstruments.common.date import (
    date_to_timestamp,
    datetime_to_timestamp,
    datetime_to_utc,
)


class FunctionTest(unittest.TestCase):
    def test_date_to_timestamp(self):
        self.assertEqual(date_to_timestamp(date(2022, 1, 1)), 1640995200000)

    def test_datetime_to_timestamp(self):
        self.assertEqual(
            datetime_to_timestamp(datetime(2022, 1, 1, 0, 0, 0)), 1640995200000
        )

    def test_datetime_to_utc(self):
        tz = timezone("US/Eastern")
        dt = datetime(2022, 1, 1, 5, 0, 0)
        dt_tz = tz.localize(datetime(2022, 1, 1, 0, 0, 0))

        self.assertNotEqual(datetime_to_utc(dt), dt_tz)
        self.assertEqual(datetime_to_utc(dt), datetime_to_utc(dt_tz))
        self.assertEqual(dt, datetime_to_utc(dt_tz))

    def test_datetime_to_utc_daylight_savings(self):
        tz = timezone("US/Eastern")
        dt = datetime(2022, 7, 1, 4, 0, 0)
        dt_tz = tz.localize(datetime(2022, 7, 1, 0, 0, 0))

        self.assertNotEqual(datetime_to_utc(dt), dt_tz)
        self.assertEqual(datetime_to_utc(dt), datetime_to_utc(dt_tz))
        self.assertEqual(dt, datetime_to_utc(dt_tz))

    def test_datetime_tz_to_timestamp(self):
        tz = timezone("US/Eastern")
        dt = datetime(2022, 1, 1, 5, 0, 0)
        dt_tz = tz.localize(datetime(2022, 1, 1, 0, 0, 0))

        self.assertEqual(datetime_to_timestamp(dt_tz), datetime_to_timestamp(dt))

    def test_datetime_tz_to_timestamp_daylight_savings(self):
        tz = timezone("US/Eastern")
        dt = datetime(2022, 7, 1, 4, 0, 0)
        dt_tz = tz.localize(datetime(2022, 7, 1, 0, 0, 0))

        self.assertEqual(datetime_to_timestamp(dt_tz), datetime_to_timestamp(dt))
