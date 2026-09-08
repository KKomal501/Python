#Read Basic Pay
bp = float(input("Enter Basci Pay:"))
#Calculate Gross Salary
hra = 0.10*bp
ta = 0.05*bp
gs = bp + hra + ta
professional_tax = 0.02*gs
#net salary
salary = gs - professional_tax
#Display Result
print("net salary:",salary)
