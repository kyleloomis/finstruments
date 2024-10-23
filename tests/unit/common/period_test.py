import unittest
from datetime import datetime, date

from dateutil.relativedelta import relativedelta

from finstruments.common.date.enum import TimeUnit
from finstruments.common.period import Period


class PeriodTest(unittest.TestCase):
    def compare_dates(self, date_first: date, date_second: date):
        self.assertEqual(date_first.strftime("%y-%m-%d"), date_second.strftime("%y-%m-%d"))

    def test_period_advance(self):
        d = datetime.now().date()

        self.compare_dates(Period(unit=TimeUnit.DAY, n=1).advance(d), d + relativedelta(days=1))
        self.compare_dates(Period(unit=TimeUnit.WEEK, n=2).advance(d), d + relativedelta(weeks=2))
        self.compare_dates(Period(unit=TimeUnit.MONTH, n=5).advance(d), d + relativedelta(months=5))
        self.compare_dates(Period(unit=TimeUnit.YEAR, n=2).advance(d), d + relativedelta(years=2))
