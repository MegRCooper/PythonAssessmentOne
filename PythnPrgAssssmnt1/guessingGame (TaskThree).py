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
