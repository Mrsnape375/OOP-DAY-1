class Animals:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(f"{self.name} is eating!")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animals):
    def flee(self):
        print(f"{self.name} is fleeing!")
class Predator(Animals):
    def hunt(self):
        print(f"{self.name} is hunting!")

class Rabbit(Prey):
    def speak(self):
        print("Sniff sniff...")
class Hawk(Predator):
    def speak(self):
        print("SKREEEEE!")
class Fish(Predator,Prey):
    def speak(self):
        print("Fish and Chips...")

rabbit=Rabbit("Bugs")
hawk=Hawk("Tony")
fish=Fish("Nemo")


rabbit.eat()
rabbit.sleep()
rabbit.flee()
rabbit.speak()
print()

hawk.eat()
hawk.sleep()
hawk.hunt()
hawk.speak()
print()

fish.eat()
fish.sleep()
fish.hunt()
fish.flee()
fish.speak()