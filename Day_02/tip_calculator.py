print("Welcome to 'TIP CALCULATOR'")

bill = float(input("Total amount of bill : "))
tip = float(input("Percentage would you like to tip : "))
numPer = int(input("How many people to split the bill : "))

t_amount = round((bill + (bill * tip / 100)) / numPer, 2)
print(f"Each person has to pay {t_amount}")
print("Thank you !")