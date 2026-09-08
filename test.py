#programe to calculate result and print
eng=float(input("enter english marks"))
mat=float(input("enter maths marks"))
sci=float(input("enter sci marks"))
hin=float(input("enter hin marks"))
if 35<=eng<=65:
    print(" improve")
if 65<=eng<=100:
    print("exellent")
if 0<=eng<=35:
        print("bc")
if 35<=mat<=65:
    print("-_-")
if 65<=mat<=100:
    print("exellent")
if 0<=mat<=35:
    print("-_-")    
if 35<=sci<=65:
    print("improve")
if 65<=sci<=100:
    print("exellent")
if 0<=sci<=35:
        print("bc")  
if 35<=hin<=65:
    print("improve")
if 65<=hin<=100:
    print("exellent")
if 0<=sci<=35:
        print("bc")           
if eng>=35 and mat>=35 and sci>=35 and hin>=35:
    print ("you have passed good boyyyy")
    tot=eng+mat+sci+hin
    avg=tot/4
    print("the total marks =",tot)
    print("the average marks =",avg)
else:
    print("you have failed padh le thoda ")