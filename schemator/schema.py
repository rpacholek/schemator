from typing import Any, Mapping, Tuple, List
from .aschema import AbstractSchema
from .typecheck import check


class Schema(AbstractSchema):
    @classmethod
    def validate_errors(cls, obj: Mapping[str, Any]) -> List[str]:
        errors = []
        error = True
        for name, objtype in cls.__annotations__.items():
            suberr = check(obj.get(name), objtype)
            if suberr:
                error = False
                if suberr:
                    errors.extend([f"{name}::{err}" for err in suberr])
                else:
                    errors.append(name)
        return errors
