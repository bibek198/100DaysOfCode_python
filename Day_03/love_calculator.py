print("Welcome to love calculator")

name1 = input("Give the first person name : ")
name2 = input("Give the second person name : ")

name = (name1 + name2).lower()

T = name.count("t") 
R = name.count("r")
U = name.count("u")
E = name.count("e")
L = name.count("l")
O = name.count("o")
V = name.count("v")
true = T + R + U + E
love = L + O + V + E

score = int(str(true) + str(love))

if (score < 10 or score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score > 40 and score < 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")


