#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from unittest.mock import Mock, patch
from typing import List, Dict, Mapping, Any, Union, Optional

from schemator.typecheck import check, is_advanced, AbstractSchema


class BasicTypeTest(unittest.TestCase):
    def assertEmpty(self, value):
        self.assertSequenceEqual(value, [])

    def assertNotEmpty(self, value):
        self.assertNotEqual(value, [])

    def test_int(self):
        self.assertEmpty(check(10, int))
        self.assertEmpty(check(0, int))
        self.assertEmpty(check(-10, int))

        self.assertNotEmpty(check(None, int))
        self.assertNotEmpty(check("String", int))
        self.assertNotEmpty(check(10.0, int))
        self.assertNotEmpty(check([], int))

    def test_none(self):
        self.assertEmpty(check(None, type(None)))

        self.assertNotEmpty(check(10, type(None)))

    def test_string(self):
        self.assertEmpty(check("string", str))

        self.assertNotEmpty(check(10, str))
        self.assertNotEmpty(check(None, str))

    def test_float(self):
        self.assertEmpty(check(10.0, float))

        self.assertNotEmpty(check(10, float))
        self.assertNotEmpty(check(None, float))

    def test_bool(self):
        self.assertEmpty(check(True, bool))
        self.assertEmpty(check(False, bool))

        self.assertNotEmpty(check(10, bool))
        self.assertNotEmpty(check(None, bool))

    def test_list(self):
        self.assertEmpty(check([], list))
        self.assertEmpty(check([10], list))
        self.assertEmpty(check([10, "assd"], list))

        self.assertNotEmpty(check(10, list))
        self.assertNotEmpty(check(None, list))

    def test_dict(self):
        self.assertEmpty(check(dict(), dict))
        self.assertEmpty(check({"test": 1, "test2": "test2"}, dict))

        self.assertNotEmpty(check(10, dict))
        self.assertNotEmpty(check(None, dict))


class AdvanceTypeTest(unittest.TestCase):
    def assertEmpty(self, value):
        self.assertSequenceEqual(value, [])

    def assertNotEmpty(self, value):
        self.assertNotEqual(value, [])

    def test_list(self):
        self.assertEmpty(check(["string", "string2", "string3"], List[str]))
        self.assertEmpty(check([], List[str]))

        self.assertNotEmpty(check(["string", 10, 20], List[str]))
        self.assertNotEmpty(check([20, 10, 20], List[str]))

    def test_dict(self):
        self.assertEmpty(
            check({
                "string": "str",
                "string2": "str"
            }, Dict[str, str]))
        self.assertEmpty(check(dict(), Dict[int, str]))

        self.assertNotEmpty(check({
            "string": "str",
            "str": 10
        }, Dict[str, int]))
        self.assertNotEmpty(check({10: "str", "str": "str"}, Dict[str, int]))

    def test_union(self):
        self.assertEmpty(check("test", Union[str, int]))
        self.assertEmpty(check(10, Union[str, int]))

        self.assertNotEmpty(check("str", Union[float, int]))


class ExampleSchema(AbstractSchema):
    @classmethod
    def validate_errors(cls, obj: Mapping[str, Any]) -> List[str]:
        return True

    @classmethod
    def load(cls, obj: dict) -> "AbstractSchema":
        return None


class OtherSchemaTest(unittest.TestCase):
    def test_other_schema(self):
        assert check({}, ExampleSchema)

    def test_other_schema_fail(self):
        with patch.object(ExampleSchema, 'validate_errors',
                          return_value=False):
            assert not check({}, ExampleSchema)


class IsAdvancedTest(unittest.TestCase):
    def test_list(self):
        assert is_advanced(List[str])
        assert is_advanced(List[int])
        assert is_advanced(List[ExampleSchema])

        assert is_advanced(List)

    def test_dict(self):
        assert is_advanced(Dict[str, str])
        assert is_advanced(Dict[str, int])
        assert is_advanced(Dict[str, ExampleSchema])

        assert is_advanced(Dict)

    def test_option(self):
        assert is_advanced(Optional[str])
        assert is_advanced(Optional[int])
        assert is_advanced(Optional[ExampleSchema])

    def test_union(self):
        assert is_advanced(Union[str, int])
        assert is_advanced(Union[int, None])
        assert is_advanced(Union[str, ExampleSchema])

    def test_any(self):
        assert is_advanced(Any)

    def test_non_advance(self):
        assert not is_advanced(int)
        assert not is_advanced(str)
        assert not is_advanced(list)
        assert not is_advanced(dict)
        assert not is_advanced(None)
        assert not is_advanced(ExampleSchema)
