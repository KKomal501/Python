# input() = A function that prompts the user to enter data.
#           Returns the entered data sa a string.

# input("")

# So, it gives you a space to eneter data when you run it.
# Check this now.

# input("What is your name?: ")

# When you enter the data, it will give you it in the form of strings.
# Now to print or use it you have to place it in a variable.

# name = input("What is your name?: ")

# age = input("What is your age?: ") 

# print(f"Your feakin' name is {name}")

# print(f"You've been troubling this world for last {age} years.")

# You've already seen how you have used the enetred data using the above code.

# Now Check this out:

# apples_1 = input("How many apples do you have?: ")
# apples_2 = apples_1 + 1
# print(f"If I give you another one, you will have: {apples_2}")

# Well, you'll find an error, cuz you can't mathematical funtions on str.
# Inorder to use that data in this way, you have to change it into int form.

# apples_1 = input("How many apples do you have?: ")
# apples_1 = int(apples_1)
# apples_2 = apples_1 + 1
# print(f"If I give you another one, you will have: {apples_2} apples.")

# It will work now. You can run mathematical functions on the data you entered now.

# Now, instead of taking an extra line to convert the variable type, we can directly do it:

# apples_1 = int(input("How many apples do you have?: "))
# apples_2 = apples_1 + 1
# print(f"If I give you another one, you will have: {apples_2} apples.")

# It works the same way!
