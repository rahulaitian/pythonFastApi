class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def drive(self):
        print(f"The {self.year} {self.make} {self.model} is now driving.")
my_car = Car("Toyota", "Corolla", 2022)
my_car.drive()