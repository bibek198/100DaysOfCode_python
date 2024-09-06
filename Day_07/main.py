import random
from hangman_words import word_list
from hangman_art import stages, logo
####################################
myWord = random.choice(word_list)
mylist = []
for i in range(0, len(myWord)):
    mylist.append("_")

end_of_game = False
lives = 6
#####################################
print(logo)
print("Guess the word: ")
print(mylist)
print(stages[6])

while not (end_of_game):
    guess = input("Guess the letter : ").lower()
    if guess in myWord:
        for i in range(len(myWord)):
            if guess == myWord[i]:
                mylist[i] = guess
        print(mylist)
        # print(stages[lives])
    else:
        lives = lives - 1
        if lives != 0:
            print(stages[lives])
            print(mylist)
        else:
           print(stages[lives]) 
               
    if "_" not in mylist:
        end_of_game = True
        print("You won !")
    if lives == 0:
        end_of_game = True
        print("You loss !")