from typing import List, Optional
from schemator.schema import Schema

class TaskType(Schema):
    name: str
    test: str
    inttest: int

class Task(Schema):
    name: str = "name"
    mode: int
    entries: TaskType

    __strict__ = False # Default


task1 = {
    "name": "test",
    "mode": 1,
    "entries": {
        "name": "test",
        "test": "test",
        "inttest": 10
        } 
}

task2 = {
    "name": "test",
    "mode": None,
    "entries": {
        "name": "test",
        "test": 10,
        "inttest": 10
        } 
}


print(Task.validate_failed(task1))
print(Task.validate_failed(task2))

print(Task.validate(task1))
print(Task.validate(task2))
