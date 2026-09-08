# Lists - A built-in data type that stores a collection of items in a particular order.
# Lists are mutable (they can be changed after creation).

# 1. Creating a List
# Can store different data types together.
my_list = [1, 2, "Python", 3.5, True]
print(my_list)

# 2. Accessing Elements
# Uses zero-based indexing.
print(my_list[0])  # First element (1)
print(my_list[-1]) # Last element (True)

# 3. List Slicing
# list[start : stop : step] - stop index is excluded.
nums = [0, 10, 20, 30, 40, 50]
print(nums[1:4])   # [10, 20, 30]
print(nums[::-1])  # Reverses the list

# 4. Modifying Lists (Mutability)
nums[0] = 100      # Changes the value at index 0
print(nums)

# --- List Methods ---

# .append(val) - Adds an element to the end of the list.
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)

# .insert(index, val) - Adds an element at a specific position.
fruits.insert(1, "orange")
print(fruits)

# .remove(val) - Removes the first occurrence of a specific value.
fruits.remove("banana")
print(fruits)

# .pop(index) - Removes and returns the element at the given index (default is last).
last_item = fruits.pop()
print(last_item)

# .clear() - Removes all elements from the list.
# fruits.clear()

# .index(val) - Returns the index of the first occurrence of a value.
index_of_apple = fruits.index("apple")

# .count(val) - Returns how many times a value appears.
numbers = [1, 2, 2, 3, 2]
print(numbers.count(2))

# .sort() - Sorts the list in ascending order (modifies original list).
numbers.sort()
# .reverse() - Reverses the order of the list.
numbers.reverse()

# 5. List Length
print(len(numbers)) # Returns the number of items in the list

# 6. Checking Existence
if "apple" in fruits:
    print("Yes, apple is in the list!")