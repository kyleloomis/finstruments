"""
Date and time functions.
"""
import calendar
from datetime import date, datetime, time
from typing import List

import pytz
from pandas import to_datetime, bdate_range


def date_to_timestamp(as_of_date: date) -> int:
    """
    Convert date to epoch timestamp in milliseconds.

    Args:
        as_of_date (date): Python date

    Returns:
        int: Epoch timestamp in milliseconds
    """
    return calendar.timegm(as_of_date.timetuple()) * 1000


def datetime_to_timestamp(dt: datetime) -> int:
    """
    Convert datetime to epoch timestamp in milliseconds.

    Args:
        dt (datetime): Python datetime

    Returns:
        int: Epoch timestamp in milliseconds
    """
    return calendar.timegm(dt.utctimetuple()) * 1000


def datetime_to_utc(dt: datetime) -> datetime:
    """
    Standardize datetime to UTC. Assume that datetime where `tzinfo=None` is already in UTC.

    Args:
        dt (datetime): Python datetime

    Returns:
        datetime: Python datetime with standardized UTC timezone (`tzinfo=None`)
    """
    # assume that datetime without timezone is already in UTC
    if dt.tzinfo is None:
        return dt
    return dt.astimezone(pytz.utc).replace(tzinfo=None)


def date_to_datetime(
        as_of_date: date, as_of_time: time = datetime.min.time()
) -> datetime:
    """
    Convert date and optional time to datetime. NOTE: time should not contain a timezone or else offset may not be
    correct.

    Args:
        as_of_date (date): Python date
        as_of_time (time): Python time

    Returns:
        datetime: Python datetime
    """
    return datetime.combine(as_of_date, as_of_time)


def create_dates_between(start: date, end: date, frequency: str = "B") -> List[date]:
    """
    Create dates between start and end date (inclusive). Frequency used to determine which days of the week are used.

    Args:
        start (date): Python date
        end (date): Python date
        frequency (str): Frequency for date range

    Returns:
        List[date]: List of dates
    """
    return [
        dt.date()
        for dt in to_datetime(
            bdate_range(start=start, end=end, freq=frequency).to_list()
        )
    ]
