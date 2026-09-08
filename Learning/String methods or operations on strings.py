# String Methods
# Can be written in:

# Double quotes
str1 = "This is a string" 

# Signle quotes
str2 = 'This is a string'

# Triple quotes
str3 = """This is a string"""

# Escape Sequence Characters: Used for formatting of strings

# "\n" = next line
str4  = "This is a string.\nThis one is for second line!"
print(str4)

# "\t" = gives a tab space between sentences
str5 = "This is a string.\tThis is a string after a Tab space."
print(str5)

# String Operations:

# 1) Concatenation{"+"}:  Adding or joining of strings.

str6 = "hello" 
str7 = "world"
sum1 = str6 + " " + str7    # It is not possible to subtract strings in the same way.
# Adding variables and raw strings is valid!
print(sum1)

# 2) length of str{"len()"}: Finds length of string

str8 = "Ffaa!!"
len1 = len(str8)
print(len1)

# It can also tell lenght of concatenated strings. 
print(len(sum1))
# Space and special characters($..,etc)is also a character and it is also counted by this command.

# 3) Indexing: Used to find character of string by their positions

# Note: Using indexing,  we can only access the character, we cannot assing or modify characters!!!

# Counting in python starts from "0"

str9 = "Karri_Komal"
ind1 = str9[2]
print(ind1)

# 4) Slicing: Used to find characters based on the range of their indexes

# str[starting_ind : ending_ind]

# staring ind is included, but ending ind is excluded.
# So if wanted to print from ind= 1 to ind= 6 (str[1:7]) 

slc1 = (str9[3:11]) # We can include last character this way
print(slc1)

slc2 = (str9[3:len(str9)]) # We can include last character this way too
print(slc2)

slc3 = (str9[3:]) # Works like str(str9[3:len(str9)])
print(slc3)

slc4 = (str9[:5]) # Works like str(str9[0:5])
print(slc4) 

# Python also assings NEGATIVE INDEXES for each characters
# It is "-1" for last character, and "-2" for last second and so on...
# When we want to slice using neg indexes, it goes like this:
slc5 = (str9[-4:-1])
print(slc5)
# In this case also, ending index is not inclued...

# str.endswith("any_string") : Checks if string ends with "any_string"
# TRUE if it ends with tht, FALSE if doesnot.

str10 = "xyz@gmail.com"
end1 = str10.endswith("@gmail.com")
print(end1)

# str.capitalize() : Capitalizes first character
str11 = "karry is napolean"
str11c= str11.capitalize()
print(str11c)

# str.replace(old_char(s), new_char(s)) - replaces characters(s) with new ones
str11n= str11c.replace("r","s")
print(str11n)

# str.find(word) - returns 1st index of 1st occurence
# If we try to find a substring which doesnot exist, it gives "-1" as output.
# Only slicing is something in which negative indexes exists.
str11f= str11.find("a")
print(str11f)

# str.count("am") - counts the occurence of substring

str12= "Badal is booty booty."
str12= str12.count("booty")
print(str12)