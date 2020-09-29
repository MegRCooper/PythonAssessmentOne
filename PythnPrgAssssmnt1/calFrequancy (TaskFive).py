'''
Step One) Define a function (cal_frequency) 
Step Two) Take a user input (String)
Step Three) Calculate the frequency of each letter of the alphabet in the input
   Step 3.1: While loop till end of user input
   Step 3.2: if/ else loop to find the frequencies.
   Step 3.3: count 
Step four) Sort the letters from the most to the least frequent
Step five) Displays the corresponding frequencies. 

Note the function should return nothing but print each letter and its 
corresponding frequency, in descending order. Treat upper and lower case 
characters of the same letter as being identical (e.g. a exists in Anna twice, 
not once; A exists in Anna twice, not once) '''

def calFrequency (): #Step One
    usersStr = input("Please enter your string: ").lower() #Step Two
    usersStr = usersStr.replace(" ", "") # Removal of the spaces
    freq = {} # Dictionary to save chars to.
    for char in usersStr: #Step 3
        if char in freq: 
            freq[char] += 1
        else: 
            freq[char] = 1
    for i in (freq):
        freqSorted = (sorted(freq.items(), key = lambda item: item [1])) # Step Four
    print(freqSorted [:: -1]) # Step 5, String slicing to iterate backwards
calFrequency()