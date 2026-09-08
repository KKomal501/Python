# Function - Block of statements that perform a specific task.
# Function operates on parameters (or) variables.
# It is used to reduce "Redundancy" code.

# def fn_name(parameter1, parameter2,...) : 
#        Some work(code)
#        return value

# "return" gives output to the exact location where function was called.
# It is also used to end functions.


# To call the function, fn_name(arg1, arg2), arguments are the values supplied.

# Exmaple_1 -

def ex_fn(a,b) :    # All this
      sum = a + b   # is called
      return sum    # function definition

sum1 = ex_fn(6,4)
print(sum1)

# Example_2 - 

# A function without parameter and who donot return anything is also possible -

def ex2_fn():
      print("Badal")

ex2_fn() # If it is placed in a variable and if you try to print variable, it will return none.


# Default Parameters - 
# If a funtions is designed to have a non-zero number of parameters, to make it work even without parameters, we add default parameters.

def ex_fn1(a,b):   # If not arguments are not give, it will return error.
      print(a*b)

def ex_fn1(a=2,b=3):   # If no values is entered, it will take a=2 and b=3 automatically.  
      print(a*b)

def ex_fn(a, b=3):    # It is possible to give default value to only one parameter.
      print(a*b)      # But parameters with default values are always written at the last.