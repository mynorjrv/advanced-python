from dataclasses import dataclass
import json

class Vehicle:
    def __init__(
        self,
        regitration_number: str,
        year_of_production: int,
        passenger: bool,
        mass: float
    ):
        ...
        
    
Vehicle(1, 123213, False, 1.251212)
