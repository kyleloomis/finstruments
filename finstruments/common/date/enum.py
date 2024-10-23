"""
Enums for payment frequency, day count convention and period.
"""

from finstruments.common.base_enum import BaseEnum


class PaymentFrequency(BaseEnum):
    """
    Payment frequency used to discount cashflows and accrue interest.
    """

    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    SEMI_MONTHLY = "SEMI_MONTHLY"
    MONTHLY = "MONTHLY"
    SEMI_QUARTERLY = "SEMI_QUARTERLY"
    QUARTERLY = "QUARTERLY"
    TRI_ANNUALLY = "TRI_ANNUALLY"
    SEMI_ANNUALLY = "SEMI_ANNUALLY"
    ANNUALLY = "ANNUALLY"

    def __int__(self):
        if self == PaymentFrequency.DAILY:
            return 252
        elif self == PaymentFrequency.WEEKLY:
            return 52
        elif self == PaymentFrequency.SEMI_MONTHLY:
            return 26
        elif self == PaymentFrequency.MONTHLY:
            return 12
        elif self == PaymentFrequency.SEMI_QUARTERLY:
            return 6
        elif self == PaymentFrequency.QUARTERLY:
            return 4
        elif self == PaymentFrequency.TRI_ANNUALLY:
            return 3
        elif self == PaymentFrequency.SEMI_ANNUALLY:
            return 2
        elif self == PaymentFrequency.ANNUALLY:
            return 1
        else:
            raise Exception(f"PaymentFrequency '{self}' not supported")


class DayCountConvention(BaseEnum):
    """
    Day count convention to determine how interest accrues over payment periods.
    """

    # Actual/360: Number of days between dates divided by 360
    ACTUAL_360 = "ACTUAL_360"

    # Actual/364: Number of days between dates divided by 364
    ACTUAL_364 = "ACTUAL_364"

    # Actual/365 FIXED: Number of days between dates divided by 365
    ACTUAL_365F = "ACTUAL_365F"

    # Actual/365_2425: Number of days between dates divided by 365.25
    ACTUAL_365_2425 = "ACTUAL_365_2425"

    def __float__(self):
        if self == DayCountConvention.ACTUAL_360:
            return 360
        elif self == DayCountConvention.ACTUAL_364:
            return 364
        elif self == DayCountConvention.ACTUAL_365F:
            return 365
        elif self == DayCountConvention.ACTUAL_365_2425:
            return 365.2425
        else:
            raise Exception(f"DayCountConvention '{self}' not supported")

    def __int__(self):
        return int(float(self))


class TimeUnit(BaseEnum):
    """
    Time unit.
    """

    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"
    YEAR = "YEAR"


class CompoundingConvention(BaseEnum):
    SIMPLE = "SIMPLE"
    COMPOUNDED = "COMPOUNDED"
    CONTINUOUS = "CONTINUOUS"
    SIMPLE_THEN_COMPOUNDED = "SIMPLE_THEN_COMPOUNDED"
    COMPOUNDED_THEN_SIMPLE = "COMPOUNDED_THEN_SIMPLE"


class Frequency(BaseEnum):
    NO_FREQUENCY = "NO_FREQUENCY"
    ONCE = "ONCE"
    ANNUAL = "ANNUAL"
    SEMIANNUAL = "SEMIANNUAL"
    EVERY_FOURTH_MONTH = "EVERY_FOURTH_MONTH"
    QUARTERLY = "QUARTERLY"
    BIMONTHLY = "BIMONTHLY"
    MONTHLY = "MONTHLY"
    EVERY_FOURTH_WEEK = "EVERY_FOURTH_WEEK"
    BIWEEKLY = "BIWEEKLY"
    WEEKLY = "WEEKLY"
    DAILY = "DAILY"


class BusinessDayConvention(BaseEnum):
    """
    Business day convention
        FOLLOWING: The date is corrected to the first working day that follows.

        MODIFIED_FOLLOWING: The date is corrected to the first working day after that, unless this working day is in the
         next month; if the modified working day is in the next month, the date is corrected to the last working day
         that appears before, to ensure the original The date and the revised date are in the same month.

        PRECEDING: Correct the date to the last business day that Preceding before.

        MODIFIED_PRECEDING: Modify the date to the last working day that appeared before, unless the working sunrise is
         now the previous month; if the modified working sunrise is now the previous month, the date is modified to the
         first working day after that The original date and the revised date are guaranteed to be in the same month.

        UNADJUSTED: No adjustment.
    """

    FOLLOWING = "FOLLOWING"
    MODIFIED_FOLLOWING = "MODIFIED_FOLLOWING"
    PRECEDING = "PRECEDING"
    MODIFIED_PRECEDING = "MODIFIED_PRECEDING"
    UNADJUSTED = "UNADJUSTED"


SECONDS_IN_MINUTE = 60
MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24
DAYS_IN_WEEK = 7

SECONDS_IN_DAY = SECONDS_IN_MINUTE * MINUTES_IN_HOUR * HOURS_IN_DAY
