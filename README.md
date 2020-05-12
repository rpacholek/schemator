# schemator

Validate the basic object the pythonic way.

The primary drive for this project is to validate the configurations.

## Example

```python
class Example(Schema):
  name: str
  mode: int
  config: Dict[str, Any]
  object: OtherSchema

example = {
  "name": "string",
  "mode": 10,
  "config": {
    "example": "param"
  },
  "object": {
    "other": "schema validation"
  }
}

Example.validate(example) # True
obj = Example.load(example)

obj.name # "string"
```

## TODO

  - [ ] Load data into struct
  - [ ] Custom types (Choice, Detect)
  - [ ] Inject a type
  - [ ] Inherit annotations
  - [ ] Config for struct (strict, allow optional default)

## License

This project is licensed under the terms of the MIT license
