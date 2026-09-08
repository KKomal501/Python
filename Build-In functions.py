# Funtions are basically of two types:
# Built-in Funtions and User-defined funtions.

# Built-in Funtions:
# 1) print() - Everything we write in the brackets of print funtions gets stored in definition of the print funtion.
# 2) len() - Same for this.
# 3) types() - Same for this.
# 4) range() - Same for this.

# 1. print() :
# One of the parameters of the print is what we enetr in the brackets.
# Two of other parameters are, 'sep' and 'end'

# sep adds a " " when we add a seperator at a place.

# This parameter is modifiable.

print("Badla", "Karri") # sep = " "
print("Badal","Karri", sep= "\n") # sep = "\n" so purpose of comma becomes printing rest in next line.


# end parameters what happens after the data enteres is printed. It's default is "\n" which means next line.

# This parameter is also modifiable.

print("Badal") # end = "\n"
print("Karri")
print("Badal", end = "|") # end = "|"
print("Karri")

# 2. len() :
# Returns number of items in a container. 
# Output is an integer.

# type() :
# Returns type of the data we enter.

# range() :
# Has three parameters - (start, stop, end)