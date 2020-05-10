from typing import List, Dict, Optional
from schemator.schema import Schema

class TaskType(Schema):
    name: str
    test: str
    inttest: int

class Task(Schema):
    name: str = "name"
    mode: int
    k: List[str]
    d: Dict[str, int]
    o: Optional[int]
    entries: TaskType

    __strict__ = False # Default


task1 = {
    "name": "test",
    "mode": 1,
    "entries": {
        "name": "test",
        "test": "test",
        "inttest": 10
        },
    "k": ["test"],
    "d": {
        "test": 1
    },
    "o": None
}

task2 = {
    "name": "test",
    "mode": None,
    "entries": {
        "name": "test",
        "test": 10,
        "inttest": 10
        },
    "o": "str"
}


print(Task.validate_errors(task1))
print(Task.validate_errors(task2))

print(Task.validate(task1))
print(Task.validate(task2))
