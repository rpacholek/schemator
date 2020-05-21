#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from unittest.mock import Mock, patch
from typing import List, Dict, Mapping, Any, Union, Optional

from schemator.schema import Schema


class SchemaLoadTest(unittest.TestCase):
    def test_basic(self):
        pairs = [
            (1, int),
            ("test", str),
            (1.0, float),
            (True, bool),
            ([], list),
            (dict(), dict)
        ]

        for v, t in pairs:
            self.assertEqual(Schema._load(v, t), v)

    def test_advanced(self):
        pairs = [
            (["test"], List[str]),
            ({"test": "test"}, Dict[str, str]),
            ({"test": 10}, Dict[str, int]),
            (10, Union[int, str]),
            ("test", Union[int, str]),
            ("test", Optional[str]),
            (None, Optional[str])
        ]

        for v, t in pairs:
            self.assertEqual(Schema._load(v, t), v)


