''' 
Step 1) Initialize function (NO arguements):
Step 2) Generate random number (1,100 inclusive):
   Step 2.1) Import the random Module:
   Step 2.2) Generate the random number: 
Step 3) Take users input of the guess (int):
Step 4) while loop till the correct number is guessed + Step 5:
Step 5) If statement in order to provide help (Comparison of numbers) :
   Step 5.1: Answer was too big (Output)
     Step 5.1.a) Add count to keep score
   Step 5.2: Answer was too small (Output) 
     Step 5.2.a) Add count to keep score
     Step 5.2.b) Ask the user to reenter a guess
   Step 5.3: Answer was correct - with the num of guesses (Output) 
     Step 5.3.a) Add count to keep score
Step 6) Output the users number of guesses
'''
import random #Step 2.1   
def guessingGame (): #Step 1
    guessNum = 1 # Sets up the counter to keep score of the users num of guesses
    randNum = random.randint (1,100) #Step 2.2
    usersGuess = int(input("What is your numberical guess (Whole numbers only) ")) #Step 3
    while usersGuess != randNum: # Step 4 (Set up of while loop only)
        if usersGuess > randNum: # Step 5.1
            print ("Your guess is too big.")
            usersGuess = int(input("Please guess again: "))
            guessNum += 1 
        elif usersGuess < randNum: #Step 5.2 
            print ("Your guess is too small.")
            usersGuess = int(input("Please guess again: "))
            guessNum += 1 
        else: #Step 5.3
            guessNum += 1 
    print ("You guessed correctly. \nYou guessed in " + str(guessNum) + " guesses.") #Step 6

guessingGame() #Calls Func. 
