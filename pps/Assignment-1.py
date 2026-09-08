# Reading Values
a = float(input("Enter first integer: "))
b = float(input("Enter second integer: "))
#Mathematical Operations
addition = a+b
subtraction = a-b
product = a*b

expression = (a+b)*(a-b)
print("Result of expression:", expression)

#Dislay Results
print("Addition:",addition)
print("Difference:",subtraction)
print("product:",product)

#Division
if b!=0:
    division = a/b
    remainder = a%b
    print("Quotient:", division)
    print("Remainder:",remainder)
else:
    print("Division is not possible.")
    