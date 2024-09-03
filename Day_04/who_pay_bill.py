import random
print("Welcome to 'Who Will Pay The Bill ?'")
names = input("Give the name of People seperated by Comman : ")

namesCSV = names.split(",")

ranName = ((random.choice(namesCSV)).upper()).strip()

print(f"{ranName} will pay the bill.")