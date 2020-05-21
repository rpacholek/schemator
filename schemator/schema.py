from __future__ import annotations
from typing import Any, Mapping, Tuple, List, Type, Dict, Union, get_origin, get_args
from .aschema import AbstractSchema, T
from .typecheck import check, is_advanced


class Schema(AbstractSchema):
    @classmethod
    def validate_errors(cls, obj: Mapping[str, Any]) -> List[str]:
        errors = []
        for name, objtype in cls.__annotations__.items():
            suberr = check(obj.get(name), objtype)
            if suberr:
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
    def validate(cls, obj: Mapping[str, Any]) -> bool:
        errs = cls.validate_errors(obj)
        return errs == []

    @classmethod
    def load(cls: Type[T], obj: dict) -> T:
        instance = cls()
        for name, objtype in cls.__annotations__.items():
            instance.__dict__[name] = cls.__load(obj.get(name, None), objtype)
        return instance

    @classmethod
    def __load(cls, value: T, objtype: type) -> T:
        if isinstance(objtype, type) and issubclass(objtype, AbstractSchema):
            return objtype.load(value)  # type: ignore
        elif is_advanced(objtype):
            if get_origin(objtype) == get_origin(List):
                args = get_args(objtype)
                if args:
                    return [cls.__load(v, args[0]) for v in value]
                return value
            elif get_origin(objtype) == get_origin(Dict):
                args = get_args(objtype)
                if len(args) == 2:
                    return {
                        key: cls.__load(v, args[1])
                        for key, v in value.items()
                    }
            elif get_origin(objtype) == Union:
                args = get_args(objtype)
                if check(value, args[0]):
                    return cls.__load(value, args[0])
                return cls.__load(value, args[1])
        else:
            return value
