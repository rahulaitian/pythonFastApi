class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def drive(self):
        print(f"The {self.year} {self.make} {self.model} is now driving.")    

class Battery:
    def __init__(self, battery_size):
        self.battery_size = battery_size
    
    def battery_info(self):
        print(f"This car has a {self.battery_size} battery.")
class ElectricCar(Car, Battery):
    def __init__(self, make, model, year, battery_size):
        Car.__init__(self, make, model, year)
        Battery.__init__(self, battery_size)   
            
    def drive(self):
        print(f"The {self.year} {self.make} {self.model} (Electric) is now driving silently.")

my_car = Car("Toyota", "Corolla", 2022)
my_car.drive()

electric_car = ElectricCar("Tesla", "Model S", 2023, "100 kWh")
electric_car.drive()
electric_car.battery_info()        