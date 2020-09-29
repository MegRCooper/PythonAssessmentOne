def calFrequency (): 
    usersStr = input("Please enter your string: ").lower() 
    usersStr = usersStr.replace(" ", "") # Removal of the spaces
    freq = {} # Dictionary to save chars to.
    for char in usersStr: 
        if char in freq: 
            freq[char] += 1
        else: 
            freq[char] = 1
    for i in (freq)
        freqSorted = (sorted(freq.items(), key = lambda item: item [1])) 
    print(freqSorted [:: -1]) 
calFrequency()
