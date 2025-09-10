#Vehicles
class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

#Animals
class Dog:
    def move(self):
        print("Running 🐕")

class Fish:
    def move(self):
        print("Swimming 🐟")

things = [Car(), Plane(), Dog(), Fish()]

for t in things:
    t.move()
