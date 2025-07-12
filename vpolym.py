class Vehicle:
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print(f"The Car engine starts,Vroom Vroom!")
class Bike(Vehicle):
    def start_engine(self):
        print(f"The Bike engine starts,Vroom Vroom!")

car=Car()
bike=Bike()

for vehicle in [car,bike]:
    vehicle.start_engine()