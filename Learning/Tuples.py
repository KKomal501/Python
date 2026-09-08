# Tuples - A built-in data type that lets us create immutable sequences of values.

tup1 = (2,3,4,5,6)

# Values can be printed using their indexes.
print(tup1[0])

# Values cannot be assinged to indexes once  a tuple is created.
# Becuase they are immutable.

# Single values tuples is in this format.
tup2 = (2,)
# If comma not places, python intereprets as tuple.

# Slicing is possible in tuples.
print(tup1[:3])
# As we know, to get values upto index 3, ending index must be 4.

# tup.index(element)- Finds at which index the element first occured.
ind = tup1.index(3)
print(ind)

# tup.count(element)- Finds how many times an element occuered in the tuple.
tup3 = (1,2,3,3,4,5,5,6)
count = tup3.count(3)
print(count)