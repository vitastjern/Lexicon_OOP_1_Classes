# Create an abstract class called Vehicle that should have abstract 
# methods drive and refuel. 
# Create2 vehicles that inherit the Vehicle class (a Car and a Truck) 
# and simulates driving and refueling them. Car and Truckboth have 
# fuel_quantity, fuel_consumption in liters per km and can be driven a 
# given distance: drive(distance) and refueled with a given amount of 
# fuel: refuel(fuel). It is summer, so both vehicles use air conditioners 
# and their fuel consumption per km when driving is increased by 0.9 
# liters for the carand with 1.6 liters for the truck. Also, the Truck has 
# a tiny hole in its tank and when it’s refueled it keeps only 95% of the 
# given fuel. The car has no problems and adds all the given fuel to its 
# tank. If a vehicle cannot travel the given distance, its fuel does not 
# change.

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def refuel(self):
        pass

class Car(Vehicle):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        # It is summer, so consumption is increased with 0.9 liters/km
        # should actually be a check on if it is summer or not and set it then
        # but this will do for now
        consumption = (0.9 + self.fuel_consumption) * distance 

        # will only drive if we have fuel for the drive 
        if consumption <= self.fuel_quantity:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):             
        # should probably check so we don't fill over the max fuel level in 
        # the tank, but thats not included in the exercise... :D
        self.fuel_quantity += fuel

class Truck(Vehicle):
    
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        # It is summer, so consumption is increased with 1.6 liters/km
        # should actually be a check on if it is summer or not and set it then
        # but this will do for now
        consumption = (1.6 + self.fuel_consumption) * distance

        # will only drive if we have fuel for the drive 
        if consumption <= self.fuel_quantity:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):             
        # should probably check so we don't fill over the max fuel level in 
        # the tank, but thats not included in the exercise... :D
        # The truck has a leak, so only 95% of the fuel is added to the tank
        self.fuel_quantity += fuel*.95


print("Car test:")
car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

print("\nTruck test:")
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
