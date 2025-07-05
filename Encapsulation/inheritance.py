#--------------------------Inheritance------------------------------------------
#Inheritance is a fundamental concept in object oriented programming that involes
#creating new classes (subclasses or derived classes) based on existing classes
#(superclasses or base classes)

#super class

class Vehicle:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting !!!")

    def stop(self):
        print("Vehicle is stopping !!!")

class Car(Vehicle):
    def __init__(self,brand,model,year,num_of_doors,num_of_wheels):
        super().__init__(brand,model,year)
        self.num_of_doors = num_of_doors
        self.num_of_wheels = num_of_wheels

class Bike(Vehicle):
    def __init__(self,brand,model,year,num_of_wheels):
        super().__init__(brand,model,year)
        self.num_of_wheels = num_of_wheels

car = Car("Ford","Focus",2008,4,4)
bike = Bike("Honda","Scoopy",2018,2)

car.start()
print(bike.__dict__)
