# logical operators = evaluate multiple conditions (or, and, not)
#                or = at least one condition must be True
#               and = both conditions must be True
#               not = inverts the condition (not False, not True)

# Practice for "or" function.

# temp = float(input("Enter the atmospheric temperature at ground level(°C): "))
# rain = input("Is it raining?(Y/N): ")

# if temp >=30 or temp <=5 or rain == "Y" :
#     print("Conditions are not suitable for the launch. The crew needs to reschedule the launch.")
# else:
#     print("Conditions are suitable for launch. The crew may proceed with further protocols.")
    
# Practice for "and" function.

# temp = float(input("Enter the atmospheric temperature at ground level(°C): "))
# rain = input("Is it raining?(Y/N): ")

# if temp >=5 and temp<=30 and rain == "N":
#     print("Conditions are suitable for launch. The crew may proceed with further protocols.")
# else:
#      print("Conditions are not suitable for the launch. The crew needs to reschedule the launch.")

# Practice for "not" function.

# if not (temp >=5 or temp<=30) and rain == "Y":
#      print("Conditions are not suitable for the launch. The crew needs to reschedule the launch.")
# elif not (temp >=30 and temp <=5)  and rain == "N":
#     print("Conditions are suitable for launch. The crew may proceed with further protocols.")
     