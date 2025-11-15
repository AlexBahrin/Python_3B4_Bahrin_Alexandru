class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, miles_driven, fuel_used):
        super().__init__(make, model, year)
        self.miles_driven = miles_driven
        self.fuel_used = fuel_used

    def calculate_mileage(self):
        return self.miles_driven / self.fuel_used if self.fuel_used != 0 else 0

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, miles_driven, fuel_used):
        super().__init__(make, model, year)
        self.miles_driven = miles_driven
        self.fuel_used = fuel_used

    def calculate_mileage(self):
        return self.miles_driven / self.fuel_used if self.fuel_used != 0 else 0

class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def get_towing_capacity(self):
        return self.towing_capacity

car = Car("Toyota", "Camry", 2022, 500, 20)
motorcycle = Motorcycle("Yamaha", "R15", 2021, 300, 10)
truck = Truck("Ford", "F-150", 2020, 13000)

print(car.get_info(), "Mileage:", car.calculate_mileage())
print(motorcycle.get_info(), "Mileage:", motorcycle.calculate_mileage())
print(truck.get_info(), "Towing Capacity:", truck.get_towing_capacity())