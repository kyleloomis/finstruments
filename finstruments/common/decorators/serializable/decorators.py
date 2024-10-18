from typing import Callable, Union

from pydantic import Field

from finstruments.common.base import Base
from finstruments.common.decorators.serializable.__util import (
    parse_obj,
    init_subclass,
    get_validators,
    convert_to_real_type,
)


def serializable(_cls: Base = None) -> Union[Callable, Base]:
    """
    This decorator adds an identifier to the decorated class for identification purposes when serializing and
    deserializing.

    NOTE: This decorator should be used on all children of base abstract classes that use the @serializable_base_class
    decorator.

    Args:
        _cls (object): The class being decorated

    Returns:
        cls: The updated class with the descriptor field
    """

    def wrap(cls):
        return type(cls.cls_name(), (cls,), {"descriptor": Field(cls.cls_name())})

    if _cls is None:
        return wrap

    return wrap(_cls)


def serializable_base_class(_cls: Base = None) -> Union[Callable, Base]:
    """
    This is a decorator sets up functionality to track all subtypes of a parent class. If you want to use a base
    class as a type signature and want the subtypes to be properly deserialized you need to add this decorator to
    the base class and @serializable to all of its children.

    NOTE: You should only use this decorator for base abstract classes

    Args:
        _cls (object): The class being decorated

    Returns:
        cls: The updated class with the descriptor field
    """

    def wrap(cls):
        setattr(cls, "_subtypes_", dict())
        setattr(cls, "parse_obj", classmethod(parse_obj))
        setattr(cls, "__init_subclass__", classmethod(init_subclass))
        setattr(cls, "__get_validators__", classmethod(get_validators))
        setattr(cls, "_convert_to_real_type_", classmethod(convert_to_real_type))
        return cls

    if _cls is None:
        return wrap

    return wrap(_cls)
