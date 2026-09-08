# Class and Object in Python

# Class is like a blueprint for creating objects.

# Creating Class
# class Student:    # Name of class is generally statrted with a capital letter.
#     name = "karan kumar"    # This means names of all students(objs) will be "karan kumar".

# This is a class called student, say it is being used for storing students data.
# Now we can create objects under this class any instance and this class will act as a blueprint for what all the object will be having.

# Creating Object(instance)
# s1 = Student()    
# print(s1)    # Will show it is an object in Student.
# print(s1.name)    # Will print "karan kumar".

# s2 = Student()
# print(s2.name)    # Will also print "karan kumar".

# ------ __init__ Function ------

# __init__ fn is a "DEFAULT CONSTRUCTOR"(Only one parameter).
# All classes have a dunction calles __init__() which is always executed when the object is being initiated.

# Creating class:
# class Student:
#      def __init__(self, fullname):
#           self.name = fullname

# Though we don't write the init funtion every single time, python itself adds an __init__ funtion when created class, every single time.
# When ever an object is created, it is executed first. Every single time.
# Infact paranthesis is added inorder to call the __init__ fn only.

# Example:-
# 
# class Student :
#     name = "Komal"
#     def __init__(self):
#         print("Adding a new student in Database...")

# s1 = Student() 
# There is no code saying to print anything in object.
# But as an object is being created in this line, the __init__ fn was executed.

# Every constructor has argument(s), in current case of __init__ , it is "self" only.
# self is nothing but the object itself. self = object. We can write anything in place of self but is conventional.
# More arguments can be added undoubtedly. We can give different names and branches to each object.

# class Student :
#     def __init__(self, name, branch):    # This is a "PARAMETERIZED CONSTRUCTOR".
#         self.name = name   # name is the one which is entered in parameter, self.name is object's name.
#         self.branch = branch
#         print("Adding a new student in Database...")
    
# s1 = Student("Raunak", "ARE")
# print(s1.name, s1.branch)


# s2 = Student("Sahil", "ARE")
# print(s2.name,s2.branch)

# Attributes : Data is attribute, any data is an attribute.

# They are of two types:
# Class attributes(Class_name.attr_name) : Common for all objects. Ex: College name for students.
# Object attributes(obj_name.attr_name) : Custom as per object. Ex: Names of students.

# In case we have same attribute, say "name" in both Class and Object.
# Preference will be give to Object attribute.

# Methods : Methods are funtions belong to objects.

# Creating class
# class Student:
#     def __init__(self,name):
#         self.name = name
#     def hello(self):    # Creating Method
#         print("hello", self.name)

# s1 = Student("karry")
# s1.hello()    # Executing Method

# Practice of so-far learned concepts.

# Create student class that takes name and marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for m in self.marks:
#             sum += m
#         avg = sum/3
#         return avg

# s1 = Student("Karry", [89, 43, 92])
# print("Hello",s1.name,"your average is",s1.get_avg())

# IT IS POSSIBLE TO CHANGE AND MANIPULATE VALUES OF ATTRIBUTES.

# For example :-
# s1.name = "Komal"
# print("Hello",s1.name,"your average is",s1.get_avg())
# It changes from Karry to Komal.

# ------STATIC METHODS------
# These are methods which donot use self.
# It works on class level.
# To create static method, we add a decorator on the top of the funtion.
# The decorator is, @staticmethod

class Student:
     def __init__(self, name, marks):
         self.name = name
         self.marks = marks


     @staticmethod
     def hello():
          print("hello")

# Now, get_avg is a static method.
s1 = Student("Karry", 95)
s1.hello()   # Nothing there in paranthesis and still no error.