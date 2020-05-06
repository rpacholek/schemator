from abc import ABC, abstractmethod
from typing import List, Tuple, TypeVar, Generic, Mapping, Any, Dict

T = TypeVar('T')

class AbstractSchema(ABC):
    @classmethod
    @abstractmethod
    def validate_failed(cls, obj: Mapping[str, Any]) -> Tuple[bool, List[str]]: pass

    @classmethod
    def validate(cls, obj: Mapping[str, Any]) -> bool:
        val, _ = cls.validate_failed(obj)
        return val

    @classmethod
    @abstractmethod
    def load(cls, obj: dict) -> "AbstractSchema": pass
