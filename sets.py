# Sets - Set is teh collection of the unordered items.
# Each element in the set must be unique and immutable. But SET as a whole is MUTABLE.
# Hence list and dictionaries cannot be stored in set.

ex_set = {1,2,3,4,"Karri"}

ex_set2 = {1,2,2,2}
# If elements repeats, they will be resolved to one single element.
# Therefore, ex_set2 will be resolved to {1,2}.

# Set has no order, it gives random order of elements each time you print.

Empty = {} # Empty dictionary.
Empty_Set = set() # Empty set.

# Set Methods :
# set.add('elements') - Adds new elements to set.

Empty_Set.add(1)
Empty_Set.add(2)
Empty_Set.add(3)
print(Empty_Set) # Will print these three elements.

# set.remove('element') - Removes mentioned element.

Empty_Set.remove(3)
print(Empty_Set) 
# If some element which doesnot even exist is attempted to be removed, it will show an error.

# set.clear() - Empties a set.
set1 = {3,5,6,4,7,9}
set1.clear()
print(set1)

# set.pop() - Picks a random value.
set2 = {3,4,5,2,1,"wooooo",("ok","gooood")}
print(set2.pop())
print(set2.pop())

# set1.union(set2) - Combines elementsof both sets and creates a new set.
uset1 = {2,23,4,5,3,7}
uset2 = {34,6,8,5,98}
print(uset1.union(uset2))
# This union is completely new set, there are no changes in the valuse of original sets.

# set1.intersection(set2) - Creates a new set contaning only common elements.
print(uset1.intersection(uset2))