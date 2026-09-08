# Temperature Inversion 

unit = input("Is this temperature in Celcius(C) or Farenhite(F)?: ")


if unit == "C":
    temp = float(input("Enter the value of temperature: "))
    result = round(temp*(9/5)+32, 2)
    print(f"Temperature in Farenheit = {result}°F")
elif unit == "F":
     temp = float(input("Enter the value of temperature: "))
     result = round((temp-32)*5/9, 2)
     print(f"Temperature in Farenheit = {result}°C")
else:
     print("Please enter the units correctly in capitals.")
