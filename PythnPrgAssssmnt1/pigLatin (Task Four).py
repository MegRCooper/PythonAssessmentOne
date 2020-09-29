'''
Step 1) Define function ()
Step 2) User input (String)
Step 3) Converstion into Piglatin.
      Step 3.1: Split the users inpt into an arr
      Step 3.2: Complete the translation of the word for all words (for loop)
         Step 3.2a: 1st letter moved to the end of the word.
         Step 3.2b: followed by the letters ay
         Here is an example: This assignment is really bizarre
         becomes histay ssignmentaay siay eallyray izarrebay  
Step 4) Returns Value as a string
'''

usersStr = input("Please enter the text you want translated into pig Latin: ") #Step 2
def pigLatin (usersStr): #Step 1
    usersStrArr = usersStr.split() #Step 3.2 
    pigLatinStr = str()
    for char in usersStrArr: #Step 3.2
        pigLatinStr = pigLatinStr + ' ' + str((char[1:] + char[0] + "ay")).lower() #Uses String slicing to move the chars.
    return (pigLatinStr) #step 4
# print(pigLatin(usersStr))