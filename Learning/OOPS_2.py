# del keyword

# Used to delete objects we might not use further to save memory.
# To use it, we simply write the del keyword and then the object.

# class Student:
#      def __init__(self, name):
#         self.name = name

# s1  = Student("Karry")
# print(s1.name) # Will print the name.

# To delete s1, we do this:
# del s1
# print(s1.name) # Will not print the name.

# To just delete the name of s1, we do this:
# del s1.name

# ------Private(like) attributes and methods------

# If we intend to put some information completely inside the class.
# If we intend to make some attributes and methods accessible only inside the class.
# We can use this there.

# By writing "__" before the attribute or method, we can make it only accessible inside the class.

# Example:
# class acc:
#         def __init__(self, name, password):
#                 self.name = name
#                 self.__password = password
#         def __reset_pswd(self):   # Here only functions inside the class can access this funtion.
#                 npwd = input("Enter new password:")
#                 self.password = npwd
        

# a1 = acc("karry", "123")
# print(a1.passwd) # Won't run as it is called outside the class.
# print(a1.name)
# reset_pswd(a1) # Won't run cuz it is called outside the class.

# --------Inheretence--------
# As the word suggests, we use this to inheret some properties like attributes or methods from one class to another class.

# For example:-

# class Car:              # In this we have basic codes required for a car.
#         @staticmethod   
#         def start():
#                 print("car started....")
        
#         @staticmethod
#         def stop():
#                 print("car stopped.")

# class ToyotaCar(Car):                  # We don't want to write our codes again and again while building Toyota cars
#         def __init__(self, brand):     # So we inhereted them from the class "Car".
#                 self.brand = brand

# class Fortuner(ToyotaCar):              # We don't want to write the code telling it is a Toyota Car everysingle time.
#         def __init__(self, type):      # So we inheret them from ToyotaCars and this goes on....
#                 self.model = type

# Now let's see the example:
# car1 = Fortuner("Diesel")
# car1.start()    # See, car has started.