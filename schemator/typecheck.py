from typing import get_origin, get_args, Any, Tuple, List, Dict, Optional, Union
from itertools import chain
from .aschema import AbstractSchema

BASIC_TYPES = [int, float, bool, str, list, dict, type(None)]
ADVANCED_TYPES = [Dict, List, Optional, Any, Union]

TError = List[str]

def check(value: Any, expected_type: type) -> TError:
    # print(value, expected_type)
    if expected_type in BASIC_TYPES:
        return _check_basic(value, expected_type)
    elif any([type(expected_type) == type(adv_type) for adv_type in ADVANCED_TYPES]):
        return _check_advanced(value, expected_type)
    elif issubclass(expected_type, AbstractSchema):
        return expected_type.validate_errors(value)
    raise NotImplementedError()


def _check_basic(value: Any, expected_type: type) -> TError:
    if expected_type in BASIC_TYPES and isinstance(value, expected_type):
        return []
    return ["TypeError"]

def _check_advanced(value: Any, expected_type: type) -> TError:
    if expected_type._name == 'List':
        if type(value) == get_origin(expected_type):
            return list(chain(*[check(val, get_args(expected_type)[0]) for val in value]))
        return ["TypeError"]
    elif expected_type._name == "Dict":
        if type(value) == get_origin(expected_type):
            result = [
                (
                    key,
                    _check_basic(key, get_args(expected_type)[0]),
                    check(val, get_args(expected_type)[1])
                ) for key, val in value.items()
            ]
            if all([k == [] for _, k, _ in result]):
                return list(chain(*[[f"{kname}::{e}" for e in err] for kname, _, err in result]))
            else:
                return ["KeyError"]
        return ["TypeError"]
    elif expected_type.__origin__ == Union:
        if any([check(value, argtype) == [] for argtype in get_args(expected_type)]):
            return []
        return ["TypeError"]
    print(expected_type.__dict__)
    print(value, expected_type, expected_type._name)
    raise NotImplementedError()
