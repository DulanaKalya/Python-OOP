class Dog:
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    
    def bark(self):
        print("Woof woof !")

class Owner:
    def __init__(self,name,address,number):
        self.name = name
        self.number = number
        self.address = address
    
    def contact(self):
        print("Name ", self.name,"/ ")
        print("Number ",self.number)





c1 = Owner("Kamal","Kandy","0900900")

print(c1.name)

dog = Dog("Rex","German Sherperd",c1)
dog.bark()

dog1 = Dog("Lassy","German Sherperd",c1)
dog1.bark()

print(dog.name)
print(dog1.breed)

print(dog1.name)
print(dog.breed)

print(dog1.owner.address)


#  ----------------------Example a person class---------------------------------

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old .")

Kamal = Person("Kamal",18)

Kamal.greet()


#-------------------------Accessing and modifying object data ------------------

from datetime import datetime

class User:
    def __init__(self,username,email,password):
        self.username = username
        self._email = email            #private attributes
        self.password = password

    def say_hi_to_user(self,user):
        print(f"sending message to {user.username} : Hi {user.username} , it's {self.username}")

    def get_email(self):
        print(f"Email accessed at {datetime.now()}")
        return self._email.lower().strip()
    
    def set_email(self,new_email):
        self._email = new_email

user1 = User("Methmi","methmi@gmail.com",20020423)
user2 = User("Nethmi","nethmi@gmail.com",48384388)

user1.say_hi_to_user(user2)



user1._email = "methmi0423@gmail.com.lk"

print(user1._email)

user1.get_email()

