from abc import ABC, abstractmethod


class DiscoverType(ABC):
    @abstractmethod
    @classmethod
    def check(cls, value, objtype: type) -> bool:
        pass

    @classmethod
    def transform(cls, value):
        return value
