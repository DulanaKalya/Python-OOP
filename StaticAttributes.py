#--------------------------Static Attributes------------------------------------

# A static attributes is an attribute that belong to belongs to the class itself ,
# not to any specific instance of the class

class User:
    user_count = 0

    def __init__(self,username,email):
        self.username = username
        self.email = email
        User.user_count +=1

    def display_user(self):
        print(f"Username: {self.username} , Email: {self.email}")

user1 = User("dulanakalya","123@gmail.com")
user2 = User("gembi","1123@gmail.com")

user1.display_user()

print(User.user_count)

print(user1.user_count)
print(user2.user_count)
