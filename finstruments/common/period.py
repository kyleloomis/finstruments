from datetime import date

from dateutil.relativedelta import relativedelta

from finstruments.common.base import Base
from finstruments.common.date.enum import TimeUnit


class Period(Base):
    """
    Period class contains n periods (e.g. 3) and time unit (e.g. MONTH).
    """

    unit: TimeUnit
    n: int

    class Config(Base.Config):
        # override to ensure that TimeUnit stays as an enum until serialized
        use_enum_values = False

    def advance(self, as_of_date: date) -> date:
        if self.unit == TimeUnit.DAY:
            return as_of_date + relativedelta(days=self.n)
        elif self.unit == TimeUnit.WEEK:
            return as_of_date + relativedelta(weeks=self.n)
        elif self.unit == TimeUnit.MONTH:
            return as_of_date + relativedelta(months=self.n)
        elif self.unit == TimeUnit.YEAR:
            return as_of_date + relativedelta(years=self.n)
        else:
            raise Exception(f"TimeUnit '{self.unit}' not supported")
