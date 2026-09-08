# Basic Calculator

operator = input("Enter the operator (=, -, *, /): ")
no_1 = float(input("Enter the first number : "))
no_2 = float(input("Enter the second number : "))

if operator == "+":
    result = float(no_1 + no_2) 
    print(f" answer = {result}")
elif operator == "_":
    result = float(no_1 - no_2)
    print(f" answer = {result}")
elif operator == "*":
    result = float(no_1 * no_2)
    print(f" answer = {result}")
elif operator == "/":
    result = float(no_1 / no_2)
    print(f" answer = {result}")