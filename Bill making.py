# Exercise Bill totaling.

print("Welcome, here is our menu : ")
print("Chicken Biriyani = Rs.130")
print("Paneer Biriyani = Rs.140")
print("Veg Biriyani = Rs.120")

input("")

print("Please enlist the items you would like to buy one by one.")

input("")

Name_1 = input("Name of the item(type 'Nill' if you want to cancel): ")

if Name_1 == "Nill" :
    qnt_1 = 0
    print("Your bill has been cancelled, Thank you")
elif Name_1!= "Nill" :
 
 qnt_1 = int(input("Enter the quanitity(type '0' if you don't want to order this item): "))
     
 if Name_1 == "Chicken Biriyani" : 
     cost_1 = 130 * qnt_1
 elif Name_1 == "Veg Biriyani" :
     cost_1 = 120 * qnt_1
 elif Name_1 == "Paneer Biriyani" :
     cost_1 = 110 * qnt_1
 else :
        print("Error!")
        print("Please restart the process followning instructions 'properly'.")

 more_1 = input("press '+' if you wan tot order more; '-' if you're done.") 

 if more_1 == "+" :
     Name_2 = input("Name of the item(type 'Nill' if you're done ordering): ")

     if Name_2 == "Nill" :
         print("You have concluded you order.")
         print(f"Total Bill = {cost_1}")
         input("")
         print("Thank you.")
     
     elif not Name_2 == "Nill" :
         qnt_2 = int(input("Enter the quanitity(type '0' if you don't want to order this item): "))
                      
         if Name_2 == "Chicken Biriyani" : 
             cost_2 = 130 * qnt_2
         elif Name_2 == "Veg Biriyani" :
              cost_2 = 120 * qnt_2
         elif Name_2 == "Paneer Biriyani" :
              cost_2 = 110 * qnt_2
         else :
             print("Error!")
             print("Please restart the process followning instructions 'properly'.")

         more_2 = input("press '+' if you want to order more; '-' if you're done.")

         if more_2 == "+" :
             Name_3 = input("Name of the item(type Nill if you're done ordering): ")

             if Name_2 == "Nill" :
                 print("You have concluded you order.")
                 print(f"Total Bill = {cost_1}")
                 input("")
                 print("Thank you.")
            
             elif not Name_2 == "Nill" :
                 qnt_3 = int(input("Enter the quanitity(type '0' if you don't want to order this item): "))
                      
                 if  Name_3 == "Chicken Biriyani" : 
                     cost_3 = 130 * qnt_3
                 elif Name_3 == "Veg Biriyani" :
                     cost_3 = 120 * qnt_3
                 elif Name_3 == "Paneer Biriyani" :
                     cost_3 = 110 * qnt_3

             elif more_2 == "-" :
                     cost_3 = 0
                     Total_3 = cost_1 + cost_2 + cost_3
                     print(f"Total Bill = {Total_3}")
                     input("")
                     print("Thank you.")
             else :
                 print("Error!")
                 print("Please restart the process followning instructions 'properly'.")

     elif more_1 == "-" :
      print(f"Total Bill = {cost_1}")
     input("")
     print("Thank you.")
 else :
        print("Error!")
        print("Please restart the process followning instructions 'properly'.")
else :
   print("Error!")
   print("Please restart the process followning instructions 'properly'.")