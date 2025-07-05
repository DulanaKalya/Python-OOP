#--------------------------------Static Methods---------------------------------

# A static method in python is a method that belongs to the class itself rather 
# than any instance of the class.

# to define static method , we use the '@staticmethod' decorator

#----------------Example of static and instant methods--------------------------

class BankAccount:
    MIN_BALANCE = 100     # static attribute

    def __init__(self,owner,balance = 0):
        self.owner = owner
        self._balance = balance

    def deposit(self,amount):
        if amount > 0:
            self._balance += amount
            self.__log_transaction("Deposit",500)
        else:
            print("check")

    def _is_valid_amount(self,amount):              # protected amount
        return amount > 0
    

    def __log_transaction(self,transaction_type,amont):       #private method
        print(f"Logging {transaction_type} of ${amont} . New balance: $ {self._balance}")


    @staticmethod
    def is_valid_interest_rate(rate):
        return 0<= rate <= 5
    
account = BankAccount("Alice",500)
account.deposit(300)