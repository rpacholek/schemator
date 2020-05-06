from typing import Any, Tuple, List, Dict, Optional, Union
from .aschema import AbstractSchema

BASIC_TYPES = [int, float, bool, str, list, dict]
ADVANCED_TYPES = [Dict, List, Optional, Any, Union]


def check(value: Any, expected_type: type) -> Tuple[bool, List[str]]:
    if expected_type in BASIC_TYPES:
        return _check_basic(value, expected_type), []
    elif issubclass(expected_type, AbstractSchema):
        return expected_type.validate_failed(value)
    raise NotImplementedError()


def _check_basic(value: Any, expected_type: type) -> bool:
    return isinstance(value, expected_type)
