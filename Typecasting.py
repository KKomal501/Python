# Typecasting = The process of converting a variable from one data type to another data type.
#               str(), int(), float(), bool()

name = "harshity"
age = 18
ch_rating = 9.7
is_ch = True

# type("name"); type(name) aese error aayega.
print(type(name))
print(type(age))
print(type(ch_rating))
print(type(is_ch))

# Now converting int to str:

age = str(age)

print(f"{age}")

# There is a difference b/w these both.
# Now let's add 1 to the new conerted variable.

# "age += 1" karke 
# print(f"{age}") karenge toh type error aayega.
# Aese mathematical operations sirph integers me hoti h.
# Abhi dekho

name = "harshity"
age = 18
ch_rating = 9.7
is_ch = True

age = str(age)

age += "1"
print(f"{age}")

# Now let's convert int to float:

name = "harshity"
age = 18
ch_rating = 9.7
is_ch = True

age = float(age)

print(f"{age}")

# Now converting float to int: 

name = "harshity"
age = 18
ch_rating = 9.7
is_ch = True

ch_rating = int(ch_rating)

print(f"{ch_rating}")

# Dekha uss decimal ko greatest integer funtion hogaya.

# Now converting str to boolean:

name = "harshity"
age = 18
ch_rating = 9.7
is_ch = True

name =  bool(name)

print(name)

# Outocme is true. Doesn't matter what's in the variable.
# No will come only if the variable was empty
# One of it's application can be like you can check if a user enters name (or) not if doesn't enters name, you can prompt them it go back and fill the name.