class car:
    def __init__(self, make, model, year):
        self.make = make 
        self.model = model 
        self.year = year 

    def drive(self):
        print(f"The {self.year} {self.make} {self.model} is now driving.")

class electricCar(car):      
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)  
        self.battery_size = battery_size

    def drive(self):
        print(f"The {self.year} {self.make} {self.model} (Electric) is now driving silently.")   

my_car = car("Toyota", "Corolla", 2022)
my_car.drive()

electric_car = electricCar("Tesla", "Model S", 2023, "100 kWh")
electric_car.drive()         