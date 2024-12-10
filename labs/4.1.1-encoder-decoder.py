from dataclasses import dataclass
from datetime import date
import json
import re
from typing import Self

class Vehicle:
    def __init__(
        self,
        regitration_number: str,
        year_of_production: int,
        passenger: bool,
        mass: float
    ):
        self.regitration_number = Vehicle.validate_registration_number(
            regitration_number
        )
        self.year_of_production = Vehicle.validate_year_of_production(
            year_of_production
        )
        self.passenger = Vehicle.validate_passenger(passenger)
        self.mass = Vehicle.validate_mass(mass)

    # Should this validations be linked to the class?
    # Should they be a module?
    @staticmethod
    def validate_registration_number(registration_number: str) -> str:
        if not isinstance(registration_number, str):
            raise TypeError('Registration number should be a str')
        if len(registration_number) != 8:
            raise ValueError(
                'Registration number should be exaclty 8 characters'
            )
        if not re.match(r'PC[a-zA-Z0-9]{6}', registration_number):
            raise ValueError(
                'Registration number dont have the correct format.'
            )
        return registration_number

    @staticmethod
    def validate_year_of_production(year_of_production: int) -> int:
        if not isinstance(year_of_production, int):
            raise TypeError('Year of production should be an int')
        if year_of_production < 1900:
            raise ValueError(
                'Year of production should be greater than 1900'
            )
        return year_of_production

    @staticmethod
    def validate_passenger(passenger: bool) -> bool:
        if not isinstance(passenger, bool):
            raise TypeError('Passenger should be a bool')
        return passenger

    @staticmethod
    def validate_mass(mass: float) -> float:
        if not isinstance(mass, float):
            raise TypeError('Mass should be a float')
        if mass <= 0:
            raise ValueError(
                'Mass cannot be negative or zero.'
            )
        return mass

    def to_json(self) -> str:
        return json.dumps(self.__dict__)
    
    @classmethod
    def from_json(cls, json_str:str) -> Self:
        return cls(**json.loads(json_str))

# @dataclass
# class Vehicle:
#     regitration_number: str
#     year_of_production: int
#     passenger: bool
#     mass: float

#     def __post_init__(self):
#         if self.year_of_production < 1900:
#             raise ValueError(
#                 'Year of production should be greater than 1900'
#             )
        
    
a = Vehicle('PC897323', 1998, False, 500.00)
print(a)
print(a.to_json())

print(Vehicle.from_json(a.to_json()))
