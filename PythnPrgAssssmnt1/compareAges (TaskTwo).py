def compareAges (): #Step One
    usersAge = int(input("Please enter your age in Years only: ")) #Step Two
    MYAGE = 19 #Step 3
    if usersAge > MYAGE: #Step 4.3
        ageDiff = usersAge - MYAGE
        print ("You are older than me by " + str(ageDiff) + " year(s).")
    elif usersAge == MYAGE: #Step 4.2
        print ("You are the same age as me.")
    else:
        ageDiff = MYAGE - usersAge #Step 4.1
        print ("You are younger than me by " + str(ageDiff) + " year(s).")
compareAges() # Call func
