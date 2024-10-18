from abc import ABC, abstractmethod
from datetime import date
from typing import List

from finstruments.common.base import Base
from finstruments.common.date import create_dates_between
from finstruments.common.decorators import serializable, serializable_base_class
from finstruments.instrument.common.cut import BaseObservationCut


@serializable_base_class
class BaseExerciseStyle(Base, ABC):
    """Exercise Style"""

    expiration_date: date
    cut: BaseObservationCut

    @abstractmethod
    def can_exercise(self, as_of_date: date) -> bool:
        """
        Returns boolean value depending on if instrument can be exercised.

        Args:
            as_of_date (date): Python date

        Returns:
            bool: Boolean value depending on if instrument can be exercised
        """
        pass

    @abstractmethod
    def get_schedule(self) -> List[date]:
        """
        Get all available dates that instrument can be exercised on.

        Returns:
            List[date]: All available dates that instrument can be exercised on
        """
        pass


@serializable
class EuropeanExerciseStyle(BaseExerciseStyle):
    """European Exercise Style"""

    def can_exercise(self, as_of_date: date) -> bool:
        """
        Returns True if date is equal to the expiration date, else False.

        Args:
            as_of_date (date): Python date

        Returns:
            bool: True if date is equal to the expiration date, else false
        """
        return as_of_date == self.expiration_date

    def get_schedule(self) -> List[date]:
        """
        Get all available dates that instrument can be exercised on - only exercise date.

        Returns:
            List[date]: All available dates that instrument can be exercised on - only exercise date
        """
        return [self.expiration_date]


@serializable
class AmericanExerciseStyle(BaseExerciseStyle):
    """American Exercise Style"""

    minimum_exercise_date: date

    def can_exercise(self, as_of_date: date) -> bool:
        """
        Returns True if date is less than or equal to the expiration date, else False.

        Args:
            as_of_date (date): Python date

        Returns:
            bool: True if date is less than or equal to the expiration date, else False
        """
        return as_of_date <= self.expiration_date

    def get_schedule(self) -> List[date]:
        """
        Get all available dates that instrument can be exercised on - all dates between minimum exercise date
        and expiration date.

        Returns:
            List[date]: All available dates that instrument can be exercised on - all dates between minimum exercise
                date and expiration date
        """
        return create_dates_between(self.minimum_exercise_date, self.expiration_date)


@serializable
class BermudanExerciseStyle(BaseExerciseStyle):
    """Bermudan Exercise Style"""

    early_exercise_dates: List[date]  # should not include expiration date

    def can_exercise(self, as_of_date: date) -> bool:
        """
        Returns True if date is contained in early exercise or expiration dates.

        Args:
            as_of_date (date): Python date

        Returns:
            bool: True if date is contained in early exercise or expiration dates
        """
        schedule = self.get_schedule()
        return as_of_date in schedule

    def get_schedule(self) -> List[date]:
        """
        Get all available dates that instrument can be exercised on - combination of early exercise and expiration
        dates.

        Returns:
            List[date]: All available dates that instrument can be exercised on - combination of early exercise and
                expiration dates
        """
        return self.early_exercise_dates + [self.expiration_date]
