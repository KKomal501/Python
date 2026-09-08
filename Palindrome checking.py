# To check if a list is palindrome.
list1 = [1,2,3,2,1]
list2 = [1,2,3,4,5]

list12 = list1.copy()
list12.reverse()
if list12 == list1 :
    print("list1 is a palindrome")
else :
    print("list1 is not a palindrome")

list22 = list2.copy()
list22.reverse()
if list22 == list2 :
    print("list2 is a palindrome")
else :
    print("list2 is not a palindrome")