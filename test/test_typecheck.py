#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from typing import List, Dict

from schemator.typecheck import check


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
        self.assertEmpty(check({"string": "str", "string2": "str"}, Dict[str, str]))
        self.assertEmpty(check(dict(), Dict[int, str]))

        self.assertNotEmpty(check({"string": "str", "str": 10}, Dict[str, int]))
        self.assertNotEmpty(check({10: "str", "str": "str"}, Dict[str, int]))


class OtherSchemaTest(unittest.TestCase):
    pass
