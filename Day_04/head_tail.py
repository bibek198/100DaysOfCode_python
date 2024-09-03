import random

seed = int(input("Give some number : "))
random.seed(seed)
# toss = random.random()
# if (toss < 0.5):
#     print("Head")
# else:
#     print("Tail")

toss = random.randint(0,1)
if (toss == 1):
    print("Head")
else: 
    print("Tail")