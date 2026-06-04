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
        