import json
from dataclasses import dataclass

@dataclass
class A:
    p: str
    q: str

@dataclass
class python_coverter_obj:
    a: A
    b: int
    c: int

simple_dict = '{"a": {"p": "q"},"b": 2,"c": 3}'
convert_to_python = json.loads(simple_dict)
obj = python_coverter_obj(**convert_to_python)
print(obj.a['p'])
