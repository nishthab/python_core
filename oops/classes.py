# clsses and object
# class is nothing but collection of attributes and methods
# attributes are characteristics of the class
# pass is used to define a empty block
# when you see bouble __ (underscore) leading and triling with any method or variable  this is nothing but
# pre define methods we are just overriding this
# A namespace is a mapping from name to object
# built in attributes like __dict___ contains class's namespace


class Account():
    '''
    This class serves the purpose of the Account
    '''

    acc_name = "jutin" # user define attributes by default they are public
    acc_no = "123450"
    __balance = 5700 # with double underscore is private we can not access the value from the object
                    # this concpt is called encapsulation this is information hiding
                    # we can access the by using methods


    # Initialization Method - Constructor
    def __init__(self, name, number):
        print("Initailizing object", self)
        self.acc_name = name
        self.acc_no = number


    # get balance
    def get_balance(self):
        return self.__balance

    # withdraw
    def withdraw(self, amt):
        self.__balance -=amt # self.__balance = self.__balance - amt
        return self.get_balance()

    # deposit
    def deposit(self, amt):
        self.__balance +=amt;
        return self.get_balance()

    # static method
    @staticmethod
    def welcome_user(name):
        return "Hello " + name + " !!! Thanks for being with us"

# object
objAcc_1 = Account("Devid", "12345")
objAcc_2 = Account("Mark", "3456",)
print("Object 1", objAcc_1)
print("Object 2", objAcc_2)

print("--------------------------------------")

print("Using class", Account.acc_name)
print("Using Object 1", objAcc_1.acc_name)
print("Using Object 2", objAcc_2.acc_name)

print("--------------------------------------")

# built in Attributes
print("Dictionary-->" , Account.__dict__)
print("Document-->", Account.__doc__)
print("Module-->", Account.__module__)
print("Bases-->", Account.__bases__) # this gives the name of the superclasses
print("Class Name-->", Account.__name__)

print("Using calss-->", Account.welcome_user(objAcc_1.acc_name))
print("Using Object:-->", objAcc_1.welcome_user("Nishtha"))

print("---------------------------------------")

# Private variables
print("Balance-->", objAcc_1.get_balance())
print("Withdraw-->", objAcc_1.withdraw(700))
print("Balance-->", objAcc_1.get_balance())
print("Deposit-->", objAcc_1.deposit(1000))
print("Balance-->", objAcc_1.get_balance())