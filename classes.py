class Student:
    def greet(self):
        print("Hello World")


student1 = Student()
student1.greet()

#initializers in python

class Student:
   def __init__(self):
        print("object created")
        
student1 = Student()
student2 = Student()

#initalize student attributes name and age

class Student:
   def __init__(self, name, age):
        self.name = name
        self.age = age
        
student1 = Student("ramesh", 35)
student2 = Student("haran", 4)

print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)

# assigning attributes for a method

class Student:
    def __init__(self, name):
        self.name = name
        
    def greet(self):    
        print("Hello", self.name)
stud1 = Student("ramesh")

stud1.greet()

# multiple student object creatins

class Student:
    def __init__(self, name):
        self.name = name
        
    def greet(self):    
        print("Hello", self.name)
stud1 = Student("ramesh")
s2 = Student("Alice")
s3 = Student("Bob")

stud1.greet()
s2.greet()
s3.greet()

# Bank account withdraw deposit functionality

class BankAccount:
    balance = 5000
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self,amount):
        self.balance -= amount
        
    
    
account = BankAccount("john", 5000)    

account.deposit(2000)
account.withdraw(4000)

print(account.balance)
        