def compareAges (): 
    usersAge = int(input("Please enter your age in Years only: ")) 
    MYAGE = 19 
    if usersAge > MYAGE: 
        ageDiff = usersAge - MYAGE
        print ("You are older than me by " + str(ageDiff) + " year(s).")
    elif usersAge == MYAGE: 
        print ("You are the same age as me.")
    else:
        ageDiff = MYAGE - usersAge 
        print ("You are younger than me by " + str(ageDiff) + " year(s).")
compareAges() 
