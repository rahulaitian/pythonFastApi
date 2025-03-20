class Car:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year
    
    @property
    def make(self):
        return self._make
    
    @make.setter
    def make(self, value):
        self._make = value
    
    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, value):
        self._model = value
    
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        if value > 1885:  # The first car was invented around this time
            self._year = value
        else:
            raise ValueError("Year must be greater than 1885.")
    
    def drive(self):
        print(f"The {self._year} {self._make} {self._model} is now driving.")

class Battery:
    def __init__(self, battery_size):
        self._battery_size = battery_size
    
    @property
    def battery_size(self):
        return self._battery_size
    
    @battery_size.setter
    def battery_size(self, value):
        if value > 0:
            self._battery_size = value
        else:
            raise ValueError("Battery size must be a positive value.")
    
    def battery_info(self):
        print(f"This car has a {self._battery_size} battery.")

class ElectricCar(Car, Battery):
    def __init__(self, make, model, year, battery_size):
        Car.__init__(self, make, model, year)
        Battery.__init__(self, battery_size)
    
    def drive(self):
        print(f"The {self._year} {self._make} {self._model} (Electric) is now driving silently.")

# Example usage
my_car = Car("Toyota", "Corolla", 2022)
my_car.drive()

electric_car = ElectricCar("Tesla", "Model S", 2023, 100)
electric_car.drive()
electric_car.battery_info()

electric_car.battery_size = 120  # Updating battery size
electric_car.battery_info()
