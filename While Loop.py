# Loops - Loops are used to repeat instructions.
# They are of two types - while loos, for loops.

# while loop - Do some work only while some condition is being satisfies.

# It will do the work as long as the condition is satisfied.

# Conditions are taken in such a way that it must end the loop at some point or else it will do it infinitely.

# For that, we generally create a count variable.

# To print "hello" five times.

i = 1
while i<= 10 :
    print("hello", i)
    i = i+1 # Or you can write i+=1

# Here, i is called an iterator. Single loop is called an iteration.

# Print numbers from 1 to 10.

i1 = 1
while i1<= 5 :
    print(i1)
    i1 += 1

# An else block can also be used with while in the same way we use with "if".

# To print the given numbers 1,4,9,16,25,36,49,81,100.

nums = [1,4,9,16,25,36,49,81,100]
i = 0
while i<len(nums) :
    print(nums[i])
    i += 1 

# Searching a number x in this tuple using loop.

nums = [1,4,9,16,25,36,49,25,100]

i = 0
while i < len(nums) :
    if nums[i] == 25:
        print(f"Number is at {i+1}th place.")
        i+=1
    else :
        i+=1

# break - Used to stop loop at the very point.
# continue - Used to "skip" loop to go to the beginning of the loop immediately at the mentioned condition.
# Ex - Skipping printing even numbers in a list of mixed numbers.
