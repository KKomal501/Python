# for loops - for loops are used for sequential transversal. For transversing list, string, tuples etc.,

exlist = [1,2,3,4]
for var in exlist : # In this for is fn, var is any varibale, and list is any list.
    print(var)    # Here, all the elemets in the list gets into var.

# For loop can be used in lists, tuples, doctionaries, strings.

# for loop in list:
list = ["ravi", "badal", "puran", "aman", "sourav"]
for name in list :
    print(name)

# for loop in tuple:
tuple = ["ravi", "badal", "puran", "aman", "sourav"]
for name in list :
    print(name)

# for loop in strings:
string = "James Cameron"
for char in string:
    print(char)

# for loop in dictionary:
dict = {
    "vivek":"badal",
    "ravi":"sir",
    "puran":"purand",
    "komal":"kari",
    "aman":"jhakar",
    "sourav":"acr"
}
for roomie in dict:
    print(roomie) # To print keys.

for nick_names in dict.values():
    print(nick_names) # To print values.

# Find a value in given list:

list = [1,4,9,16,25,36,49,64,36,100]

i = 0
for num in list :
    if num == 36 :
        print("Element found at the index:",i) 
    i += 1  # i+=1 is used out of if cuz, if it is used inside if, it will add 1 only when 36 is found.

# range()- Range functions returns a sequence of numbers, starting from 0 by default, and increments(step) by 1 by default and stops before a specific number.
# range(start?,stop,step?).These are 3 variables on which range funtion works.
# Qn mark means optional.
# Stop is not included. Start is included.

# Look at this - 
ex_range = range(5) # Means ex_range = 0,1,2,3,4.
print(ex_range[0])
print(ex_range[1]) # And so on...

# Example: 
print(range(5)) # range(5) returns 0,1,2,3,4.


# Example:
for x in range(1,6,2):
    print(x)

# Printing even numbers from 100 to 1:
for x in range(100,0,-2):
    print(x)

# Print the multiplication table for "9":
for x in range(13):
    print(9*x)

# "pass" - Null statement, kuch nhi krta.
# Agar for loop ko khali chhod de toh error aata h.
# Hence, to create a loop which does nothing, we use this.
# It is different than "continue".
# Can be used as place holder for future code.

# Example:
for i in range(10,2,-1):
    pass
print("Some useful work.") # Loop ke baad kuch useful kaam h.

# Prac
# Sum of "n" numbers.
n = int(input("Enter an integer:"))
i = 0
sum = 0
while i <= n :
    sum += i
    i+=1
print(sum)

# Factorial of number "n".
i = 1
fact = 1
while i <= n:
    fact *= i
    i += 1
print(fact)