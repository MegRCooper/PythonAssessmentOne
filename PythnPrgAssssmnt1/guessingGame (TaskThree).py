import random   
def guessingGame (): 
    guessNum = 1 
    randNum = random.randint (1,100) 
    usersGuess = int(input("What is your numberical guess (Whole numbers only) ")) 
    while usersGuess != randNum: 
        if usersGuess > randNum:
            print ("Your guess is too big.")
            usersGuess = int(input("Please guess again: "))
            guessNum += 1 
        elif usersGuess < randNum: 
            print ("Your guess is too small.")
            usersGuess = int(input("Please guess again: "))
            guessNum += 1 
        else: 
            guessNum += 1 
    print ("You guessed correctly. \nYou guessed in " + str(guessNum) + " guesses.") 

guessingGame()
