# Polymorphism

# The word polymorphism is derived from greek, and means "having multiple forms"

# poly - many , Morph - forms

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

vehicles : list[Vehicle] = [
    Car("Ford","Focus",2008,4,4),
    Bike("Honda","Scoopy",2018,2)
]

for vehicle in vehicles:
    if isinstance(vehicle,Car):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
    print(vehicle.__dict__)


