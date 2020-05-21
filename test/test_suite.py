#!/usr/bin/env python
# -*- coding: utf-8 -*-
from schemator.schema import Schema

def test_case1():
    class T1(Schema):
        a: bool
        b: int
        c: float
        d: str
        e: list
        f: dict

    t1_1_data = {
        "a": True,
        "b": 10,
        "c": 1.0,
        "d": "test",
        "e": [],
        "f": dict()
    }

    t1_2_data = {
        "a": True,
        "b": 10,
        "c": 1.0,
    }

    t1_3_data = {
        "a": 10,
        "b": True,
        "c": "str",
        "d": 10,
        "e": 10,
        "f": "test"
    }

    assert T1.validate(t1_1_data)
    assert not T1.validate(t1_2_data)
    assert not T1.validate(t1_3_data)
