#--------------------------------Getter Property--------------------------------
class Person:
    def __init__(self,username,email,password):
        self.username = username
        self._email = email
        self.password = password
    
    @property
    def email(self):
        print("Email accessed")
        return self._email.strip()
    
    def get_email(self):
        print("Email accessed")
        return self._email.strip()
    
    @email.setter
    def email(self,new_email):
        self._email= new_email


user = Person("Kamal"," kamal@gmail.com ",6767)

print(user.email)
print(user.get_email())

user.email = "newEmail@gmail.com"

print(user.email)