#import the random class
import random

#Select a random number and assign it to a variable
print("Computer picks a number between 1 -100. Can you guess what it is?")
computerNum = random.randint(1,101)

#Set variable to False, and use a while loop until user guesses correctly
correct = False
while correct == False:
    userNum = int(input("Guess a Number between 1 - 100: "))
    if userNum == computerNum:
        print("It's A Match!!!")
        correct = True
    elif userNum > 100 or userNum < 1:
        print("Only guess between 1 - 100")
    elif userNum > computerNum:
        print("Hint: Too High")
    elif userNum < computerNum:
        print("Hint: Too Low")
print("Thank you for playing")





