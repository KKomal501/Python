# 5th question

n = int(input("enter n : "))
for i in range(1, 11, 1):
    print(n, "*",i ,"=", i*n)


#6th question 

str1 = input("enter a string : ")
print(str1[0:10])

#7th question
str2 = input("enter a string : ")
print(len(str2))
print(str2[::-1])



str1 = "India is my country"
str2 = "Ireland a foreign nation"

str1_s = str1.split()
print(str1_s)
str2_s = str2.split()

for ch in str1_s:
    if ch in str2_s:
        print("match found")
    else:
        print("no match found")



str1 = input("str1 : ")
if str1 == str1[::-1]:
    print(str1,"is a palindrome")
else:
    print(str1, "is not a palindrome") 


for i in range(0, 5):
    if i == 3:
        pass
    else:
        print("Hello")


marks = [ 45,78, 62, 90, 55, 78, 90, 33, 45, 67 ]
print(marks)
print(type(marks))
print(len(marks))
print(marks.count(90))
print(marks.insert(3,50))
print(marks)
print(marks.remove(90))
print(marks)
print(marks.pop())
print(sum(marks))
average = (sum(marks)/len(marks))
print(average)



student = {
    "Name " : "Vishnu",
    "Branch " : "Are",
    "RN ": 9143,
    "Marks " : [100, 100, 100, 100, 100 ]
}

print(student)
print(type(student))
print(student["Marks "])
student["Name "] = "manoj"
print(student)


print(student.keys())