usersStr = input("Please enter the text you want translated into pig Latin: ") 
def pigLatin (usersStr): 
    usersStrArr = usersStr.split() 
    pigLatinStr = str()
    for char in usersStrArr: 
        pigLatinStr = pigLatinStr + ' ' + str((char[1:] + char[0] + "ay")).lower() #Uses String slicing to move the chars.
    return (pigLatinStr) 
