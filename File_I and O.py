# File I/O - Python can be used to perform operations on a file(read and write data).

# Types of all files -
 
# Text files : .txt, .docx, .log etc.
# Binary files : .mp4, .mov, .png, .jpeg etc.,

# We have to open the file before reading or writing it.

# f = open("file_name", "mode")
# mode = "r" for read mode ; "w" for write mode
# If mode is not given, python will assume it as read.

# f = open("demo.txt", "r") # If file is not saved in same folder, whole path must be written.

# f.read will return all the data in file.
# As we are dealing with text docs currently, it will retuen strings.

# data = f.read() 

# print(data)

# After completing the operation, being a gentle programmer, close the file.
# Use f.close to close the file.
# It removes the risk that some intruder to use data from the file.

# f.close()

#   Modes and character for them:
#   
#   'r'     open for reading(default)
#   'w'     open for writing, it ereases the file first
#   'x'     create a new file and open it for writing
#   'a'     open for writing, appending to the end of the file if it exists
#   'b'     binary mode
#   't'     text mode(default)
#   '+'     open a disk file for updating(reading and writing)
#   'r+'    read + overwrite (pointer at starting) - not truncation
#   'w+'    read + overwrite - truncates data
#   'a+'    read + append  (pointer at the end) - no truncation

# We can combine different mode, if we want to read a binary file mode = "rb"

# Reading a file - 

# data = f.read()        #reads entire file
# data = f.readline.()   # reads a file line by line

# We can enable it to read ony certain number of characters.
# f.read(5) this will print first 5 characters in the file.
# It doesnot work like index.

# f = open("demo.txt", "r")

# char = f.read(4)
# print(char) 

# See how readline works :

# line1 = f.readline()
# print(line1) # Prints first line.
#  It prints an empty line cuz the is a "/n" at the ending of each line except last line.

# line2 = f.readline()
# print(line2) # Prints next line. And this can be done until file ends.

# f.close()

# If we repeat this even after the file ends, it will give empty.
# Becuase it already read all the lines.

# If we read the whole file using f.read() then try to read lines.
# It will give empty as it already read and got past the whole file.

# Writing a file - 

# It has two modes :
#   1. "w" mode :- It erases all the data first and then writes the data.
#   2. "a" mode :- It add the data from the end.

# Example of "w" mode:
# f = open("demo.txt", "w")
# f.write("This is an example of 'w' mode.")   #  Will erase all the data and then add the entered data.
# f.close() 

# Example of "a" mode:
# f = open("demo.txt", "a")
# f.write("\nThis is an additional sentence.")
# f.close()

# If we try to write in a file which doesnot exist, python will create one for us.
# It will create and file and will save it in the same folder.

# There are a lot of modes out there which perform different operations.

#       -----BETTER SYNTAX FOR ALL THESE OPERATIONS-----

# Let's demonstrate these operations with a better structured syntax:-
# This enables us to work on file like a funtion.
# Also when we use this suntax, "WE NEED NOT WORRY ABOUT CLOSING FILE".
# It is automatically done by the syntax.

# with open("demo.txt", "r") as f:    # as means open("demo.txt", "r") is now contained in f
#     data = f.read()                 
#     print(data)

# with open("demo.txt", "w") as f:
#     wrt = f.write("This is written using better syntax.")

# These files cannot be deleted using f.delete() or something.
# We need to use modules to delete this file now.

# Modules are files in which there some useful functions written in advance.
# They are like books in a library.
# We "import" modules when we need them.
# There are some pre-installed modules, we have to download the rest from internet.

# For deleting these files, we have to import "os" module.


# Deleting file :-
# import os

# os.remove("demo.txt")

#   -------PRACTICE QUESTIONS-------

# Create a new file "practice.txt" using python. Add the following data in it:
# Hi everyone
# we are learning photography
# using realme p3 5g
# I like programming in JAVA

# with open("fileIndO.txt","w") as f:
#     f.write("Hi everyone\nwe are learning photography\nusing realme p3 5g\nI like programming in JAVA")

# WAF that replace all occurences of "JAVA" with "python" in above file.

# def replace_java_to_python():
#     with open("fileIndO.txt", "r") as f:
#      data = f.read()
# 
#     n_data = data.replace("JAVA", "python")

#     with open("fileIndO.txt", "w") as f:
#         f.write(n_data)

#     with open("fileIndO.txt", "r") as f:
#         data = f.read()
#         print(data)

# WAF to Search if "learning" exists in this file or not:

# def check_for_word():

#     with open("fileIndO.txt", "r") as f:
#        data = f.read()
#        search = data.find("learning")
#        if search != -1 :
#             print("Found")
#        else:
#             print("Not found")

# WAF to check in which line does learning appears first

# def word_line():

#     with open("fileIndO", "r") as f:

#         word = "learning"
#         line = 1
#         data = True

#         while data :
#             if f.readline().find(word) != -1:
#                 print("Found in line number", line)
#                 return
#                 line += 1
#                     # If loop finds the word, we will get out of the funtion where the line where return is written.
#     return -1       # It will return "-1" if we didnot find at all i.e, loop is ended.

# From a file containing numbers seperated by comma, print the count of the even numbers.

with open("fileIndO.txt", "w") as f:
    f.write("1, 2, 76, 84, 90, 101")

with open("fileIndO.txt", "r") as f:
    data = f.read()

lst = []
x = True

no = ""

for n in data:
    if n != "," and n != " ":
        no += n
    elif n == ",":
        no = int(no)
        lst.append(no)
        no = ""
    elif n == " ":
        continue

if no:
    lst.append(int(no))

count = sum(1 for num in lst if num%2 == 0)
print(count)