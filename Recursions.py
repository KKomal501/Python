# Recursion - Loops ka ek alternate version.
# Isme function khud hii apne aap ko baar baar call kr skta h

# We can use loops in place if reursions and recursions in place of loops anytime.

# In few situations, recursions are easier to write.


# Recursion function for printing numbers from n to 0 backwards. 

def exrec(n):
    if(n == 0 ):   # This if statement is called """BASE CASE""", it decides when to stop reucrusion program.
        return     # return without no variable written beside acts like break.
    print(n)
    exrec(n-1)

# This is a recursice function.

# Recursion function for finding factorial of a number.

def fact(n):
    if(n==0 or n==1):       # It is the "BASE CASE".
        return
    return fact(n-1) * n    # Recursive case of the funtion, the funtion which enables the function to repeat itself.

# Give sum of upto n number :

def calsum(n):
    if n == 0 :
        return 0
    return calsum(n-1) + n

# Print all items in a list :

def prnt_list(list, i=0):
    if i  == len(list) :
        return
    print(list[i])
    return prnt_list(list, i = i+1)

ex_list = [9,8,7,6,5,4]
prnt_list(ex_list)