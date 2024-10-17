"""
Common types.
"""
from datetime import date, datetime
from typing import NewType, Union

Datetime = NewType("Datetime", Union[date, datetime])
