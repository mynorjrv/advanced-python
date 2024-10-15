class Tires:
    def __init__(self, *, size=15) -> None:
        self.size = size
        self.pressure = 30

    def get_pressure(self):
        print('Returning pressure')
        return self.pressure
    
    def pump(self):
        print('Pumping xd')

class Engine:
    def __init__(self, *, fuel_type='electric'):
        self.fuel_type = fuel_type
        self.state = 'OFF'

    def start(self):
        if self.state=='OFF':
            print('Turning ON')
            self.state = 'ON'
        else:
            print('Already ON')
    
    def stop(self):
        if self.state=='ON':
            print('Turning OFF')
            self.state = 'OFF'
        else:
            print('Already OFF')

    def get_state(self):
        print(self.state)
        return self.state
    
class Vehicle:
    def __init__(
            self, 
            VIN:int=0, 
            engine:Engine=Engine(),
            tires:Tires=Tires()
            ) -> None:
        self.VIN = VIN
        self.engine = engine
        self.tires = tires


city_tires = Tires(size=15)
offRoad_tires = Tires(size=18)

electric_engine = Engine(fuel_type='electric')
petrol_engine = Engine(fuel_type='petrol')

city_car = Vehicle(
    VIN=12454, 
    engine=electric_engine, 
    tires=city_tires
)

allTerrain_car = Vehicle(
    VIN=545454,
    engine=petrol_engine,
    tires=offRoad_tires
)

allTerrain_car.engine.start()
allTerrain_car.engine.get_state()
allTerrain_car.engine.start()

allTerrain_car.tires.pump()

city_car.engine.get_state()