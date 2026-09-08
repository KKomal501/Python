# Dictionaries = Dictionaries are used to store data values in "key:value" pairs.

# Dictionaries are unordered, mutable and don't allow duplicate keys.

# Any data types can be used in both value.

# Lists and dictionaries cannot be key. Becuase thay are mutable. 
 
# Keys cannot be repeated.

dict = {
    "name" : "Karri",
    "cgpa" : "mkc uski",
    "marks" : [56,76,98.4]
}

# dict_name["key"] - Denotes the values assigned to the key.
# Ex: print(dict["name"]), prints "Karri".

print(dict["name"])
print(dict["cgpa"])
print(dict["marks"])

# If the key entered doesnot exist in dictionary, error will come.

# Dictionarires are mutable.
# dict_name["key"] = "new_value" assingns new value to the entered key.

dict["name"] = "Badal"
dict["cgpa"] = "8.46"

print(dict)

# You can also create a null dictionary and add both key-value pairs to the dictionary.
# Ex :
null ={}
null["name"] = "Reppy"
print(null)

# Nested Dictionaries
# Dictionary me dictionary hona.
# We can assing a dictionary to key.

stud = {
    "name" : "Puran",
    "subject" : {
        "physics" : 99,
        "maths" : 89,
        "chem" : "maut"
    },
    "Roll_no." : 23,
}

# If a value in the nested dictionary to be printed,
print(stud["subject"]["chem"])

# To see what all keys are there - 
print(stud.keys())
# It will only print keys outside the nested dict.

# These keys are called dict_keys we can covert dict_keys data types into list or tuples.
stud_keys = list(stud.keys())
print(stud_keys)

# To see how many keys are there - 
print(len(stud))

# To print all the values in the dict - 
print(stud.values())

# dict_name.items() - returns (key,value) pairs as tuples.
print(stud.items())

# dict_name.get("key") - Another way to get value of the key.

# This is different becuase if the entered key doesnot exist, it gives none as return.

print(stud.get("name"))

print(stud.get("name1"))

# dict_name.update(new_dict) - Inserts the specified items to the dictionary.

stud.update({"city":"vizag"})
print(stud)

# It is also possible to create a varible and create a dict in that var and update that var.

# If an already existing key is updated then, it replaces old value with new value.
# This is because no key can be repeated in dictionary.