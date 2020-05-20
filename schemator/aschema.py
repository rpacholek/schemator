from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Tuple, TypeVar, Generic, Mapping, Any, Dict

T = TypeVar('T')


class AbstractSchema(ABC):
    @classmethod
    @abstractmethod
    def validate_errors(cls, obj: Mapping[str, Any]) -> List[str]: pass

    @classmethod
    def validate(cls, obj: Mapping[str, Any]) -> bool:
        errs = cls.validate_errors(obj)
        return errs == []

    @classmethod
    @abstractmethod
    def load(cls: T, obj: dict) -> T: pass
