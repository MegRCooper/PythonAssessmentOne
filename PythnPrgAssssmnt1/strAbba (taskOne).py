''' 
Step 1) Initalise the function (NO arguments):
Step 2) Take users first input [A] (Str):
Step 3) Take users second input [B] (Str):
Step 4) return the String in [ABBA] format:
'''

def strAbba (): # Step One
    userInpA = input("Please enter your first word ") #Step Two
    userInpB = input("Please enter your second word ") #Step Three
    return(userInpA + userInpB * 2 + userInpA) #Step Four
#print(strAbba())
strAbba() # Calls Function