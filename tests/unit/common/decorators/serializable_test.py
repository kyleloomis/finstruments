import json
import unittest
from abc import ABC
from datetime import datetime
from typing import List

from pytz import timezone

from finstruments.common.base import Base
from finstruments.common.decorators.serializable import serializable, serializable_base_class


@serializable_base_class
class Parent(Base, ABC):
    x: int
    y: int


@serializable
class Foo(Parent):
    pass


@serializable
class Bar(Parent):
    pass


class Container(Base):
    foo: Parent
    bar: Parent
    generic: Parent

    collection: List[Parent]


class ContainerSquared(Base):
    container: Container


class TestAnnotatedSerialization(unittest.TestCase):
    def setUp(self) -> None:
        self.foo = Foo(x=0, y=0)
        self.bar = Bar(x=1, y=1)

    def assert_serialization(self, obj, cls):
        serialized_data = json.loads(obj.json())
        deserialized_data = cls(**serialized_data)
        self.assertEqual(obj, deserialized_data)

    def test_nested_serialization(self):
        container = Container(
            foo=self.foo,
            bar=self.bar,
            generic=self.foo,
            collection=[self.foo, self.bar],
        )
        container_squared = ContainerSquared(container=container)

        self.assert_serialization(container, Container)
        self.assert_serialization(container_squared, ContainerSquared)

    def test_updated_parent(self):
        @serializable
        class Fizz(Parent):
            pass

        fizz = Fizz(x=2, y=2)
        container = Container(
            foo=self.foo,
            bar=self.bar,
            generic=fizz,
            collection=[self.foo, self.bar, fizz],
        )
        container_squared = ContainerSquared(container=container)

        self.assert_serialization(container, Container)
        self.assert_serialization(container_squared, ContainerSquared)

    def test_datetime_tz_serialization(self):
        class A(Base):
            dt: datetime

        tz = timezone("US/Eastern")
        dt = datetime(2022, 1, 1, 5, 0, 0)
        dt_tz = tz.localize(datetime(2022, 1, 1, 0, 0, 0))

        a = A(dt=dt)
        a_tz = A(dt=dt_tz)

        self.assertEqual(a.request_dict(), {"dt": 1641013200000})
        self.assertEqual(a_tz.request_dict(), {"dt": 1641013200000})

    def test_datetime_tz_to_timestamp_daylight_savings_serialization(self):
        class A(Base):
            dt: datetime

        tz = timezone("US/Eastern")
        dt = datetime(2022, 7, 1, 4, 0, 0)
        dt_tz = tz.localize(datetime(2022, 7, 1, 0, 0, 0))

        a = A(dt=dt)
        a_tz = A(dt=dt_tz)

        self.assertEqual(a.request_dict(), {"dt": 1656648000000})
        self.assertEqual(a_tz.request_dict(), {"dt": 1656648000000})
