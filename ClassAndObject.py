class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print("Woof woof !")

dog = Dog("Rex","German Sherperd")
dog.bark()

dog1 = Dog("Lassy","German Sherperd")
dog1.bark()

print(dog.name)
print(dog1.breed)