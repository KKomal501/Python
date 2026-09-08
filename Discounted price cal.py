price = int(input("Enter price before trying discount:"))
Addn_itm_price = int(input("Enter price of additional item:"))
disc = int(input("Enter the total disc %:"))
Total = (price+Addn_itm_price) -  (price+Addn_itm_price)*10/100
print("Total price =",Total,"Rs")