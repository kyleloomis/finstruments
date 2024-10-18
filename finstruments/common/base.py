"""
Base classes with custom attributes for updating, serializing and deserializing data classes and enums.
"""

import base64
import copy
import json
from abc import ABC
from datetime import date, datetime, tzinfo
from typing import List

import pydash as _
from pydantic import BaseModel
from pydantic.utils import deep_update

from finstruments.common.date import date_to_timestamp, datetime_to_timestamp
from finstruments.common.function import to_nested_dict


class Base(ABC, BaseModel):
    """
    Base class used for all data classes.
    """

    class Config:
        # use enum values when using .dict() on object
        use_enum_values = True

        json_encoders = {
            date: date_to_timestamp,
            datetime: datetime_to_timestamp,
            tzinfo: str,
        }

    @classmethod
    def cls_name(cls) -> str:
        """
        Get class name.

        Returns:
            str: Class name
        """
        return cls.__name__

    def request_dict(self) -> dict:
        """
        Convert data class to dict. Used instead of `.dict()` to serialize dates as timestamps.

        Returns:
            dict: Serialized data class as dict
        """
        return json.loads(self.json(by_alias=True))

    def base64_encoded(self, exclude=None) -> bytes:
        """
        Base-64 encode data class.

        Returns:
            bytes: Base-64 encoded data class as bytes
        """
        json_str = json.dumps(self.json(exclude=exclude), sort_keys=True)
        bytes_rep = bytes(json_str, "utf-8")
        return base64.b64encode(bytes_rep)

    def __hash__(self):
        """
        Pydantic doesn't support hashing its base models so this is a work around

        https://stackoverflow.com/a/63774573/8189527
        """
        return hash((type(self),) + tuple(self.__dict__.items()))

    def copy(self, ignored_fields: List[str] = None, **kwargs) -> "Base":
        """
        Create a copy of the object

        Parameters:
            ignored_fields: fields to ignore from the original object when copying
            **kwargs: key value pairs of fields you want to change during the copy, for nested fields delimit the keys
            with a period (e.g. `.`)

        Returns:
            Copy of the opbject
        """
        cls = self.__class__
        obj_dict = copy.deepcopy(self.request_dict())
        ignored_fields = [] if ignored_fields is None else ignored_fields

        updated_fields = to_nested_dict(kwargs)
        obj_dict = deep_update(obj_dict, updated_fields)
        [_.unset(obj_dict, field) for field in ignored_fields]
        return cls(**obj_dict)
