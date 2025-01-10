from decimal import Decimal
import pathlib
from pathlib import Path
import xml.etree.ElementTree as ET

def celsius_to_fahrenheit(
        celsius:float
    ) -> float:
    frac = (Decimal(9)/Decimal(5))
    cel = Decimal(celsius)
    return float(frac*cel + Decimal(32))

def forecast_parser(
        file:str|Path
    ) -> None:
    tree = ET.parse(file)
    root = tree.getroot()

    for item in root:
        farenheit = celsius_to_fahrenheit(
            float(item[1].text)
        )
        print(
            f'{item[0].text}:', 
            f'{item[1].text} Celsius,',
            f'{farenheit} Farenheit',
        )

forecast_parser(
    './labs/forecast.xml'
)