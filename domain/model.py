from dataclasses import dataclass


@dataclass
class MyData:
    some_str: str
    some_float: float
    some_int: int


@dataclass
class DataWithMoreFields:
    first_str: str = None
    first_float: float = None
    first_int: int = None
    second_int: int = None
    second_str: str = None
