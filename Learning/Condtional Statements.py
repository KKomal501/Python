# Conditional Expressions
# A one line shortcut for if-else statements(ternary operators in other languages)
# X if conditon else Y 

X_1 = input("Enter the first password: ")
X_2 = input("Enter th second password: ")
X_3 = input("Enter the third password: ")

Response = "Access Granted" if X_1 == "I" and X_2 == "am" and X_3 == "Gay" else "Then Go F**K youself"
print(Response)