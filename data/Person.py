from dataclasses import dataclass

@dataclass
class Person:
    dni: int
    first_lastname: str
    second_lastname: str
    name: str
    initial_second_name: str
    gender: str
    age: int
    hours: int
    minutes: int
    seconds: int