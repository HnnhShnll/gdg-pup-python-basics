class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe(self):
        return f"This car is a {self.year} {self.make} {self.model}."

my_car = Car("Ford", "Explorer", 2023)

print(my_car.describe())