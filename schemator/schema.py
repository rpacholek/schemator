from typing import Any, Mapping, Tuple, List
from .aschema import AbstractSchema
from .typecheck import check


class Schema(AbstractSchema):
    @classmethod
    def validate_failed(cls, obj: Mapping[str, Any]) -> Tuple[bool, List[str]]:
        errors = []
        error = True
        for name, objtype in cls.__annotations__.items():
            flag, suberr = check(obj.get(name), objtype)
            if not flag:
                error = False
                if suberr:
                    errors.extend([f"{name}::{err}" for err in suberr])
                else:
                    errors.append(name)
        return error, errors
