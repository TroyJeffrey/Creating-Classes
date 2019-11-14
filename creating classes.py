# Troy Jeffrey Amegashie
# Creating Classes

import random

class Car():

    def __init__(self, make, model, color, year, price, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.price = price
        self.mileage = mileage
        self.newcolor = ['yellow', 'green', 'blue', 'brown']


    def description(self):
        print(f"This car is a "
              f"{self.year} {self.make} {self.model}"
              f". It is {self.color}"
              f". This car costs {self.price} and has {self.mileage} miles")


    def change_color(self, color2):
        self.newcolor.append(color2)
        print(f"The color changed to {color2}.")

    def update_odometer(self):
        self.mileage = self.mileage + random.randint(100, 800)
        print(f"Odometer updated. This car has {self.mileage} miles.")


car1 = Car("Honda", "Accord", "black", "2016", "$9,000", 3000)

car1.description()
car1.change_color('green')
car1.update_odometer()
