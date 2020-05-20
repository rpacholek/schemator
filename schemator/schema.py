from __future__ import annotations
from typing import Any, Mapping, Tuple, List
from .aschema import AbstractSchema, T
from .typecheck import check, is_advanced


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
        if cls.__dict__.get("__strict__", False):
            for name, _ in obj.items():
                if name not in cls.__annotations__:
                    errors.append(f"{name}::UnexptectedKey")
        return errors


    @classmethod
    def validate(cls, obj: Mapping[str, Any]) -> bool
        errs = cls.validate_errors(obj)
        return errs == []

    @classmethod
    def load(cls: Type[T], obj: dict) -> T:
        instance = cls()
        for name, objtype in cls.__annotations__.items():
            if isinstance(objtype, type) and issubclass(objtype, AbstractSchema):
                instance.__dict__[name] = objtype.load(obj.get(name))
            elif is_advanced(expected_type):
                pass
            else:
                instance.__dict__[name] = obj.get(name)
        return instance
