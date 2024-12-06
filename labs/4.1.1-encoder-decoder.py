from dataclasses import dataclass
import json

@dataclass
class Vehicle:
    regitration_number: str
    year_of_production: int
    passenger: bool
    mass: float

