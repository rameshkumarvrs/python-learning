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