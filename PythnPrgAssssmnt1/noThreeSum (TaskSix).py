'''
Step One: Write a function called “no_three_sum” (a,b,c)
Step Two: Returns their sum. 
Step Three: Write a separate helper function "def fix_three(n):
   Step 3.1.a: returns that value fixed for the rule. 
     Step 3.1.1.a: However, if the val = multiple of 3 then that val = 0
     Step 3.1.1.b: except the multiples of three between 20 and 29.
'''

def fixThree (n): #Step Three
   if n % 3 == 0 and not (n >= 20 and n <= 29): 
      n = 0 
   return n 

def noThreeSum (valA,valB,valC): #Step One
   valA = fixThree(valA)
   valB = fixThree(valB)
   valC = fixThree(valC)
   sum = (valA + valB + valC) #Step Two
   return (sum)

noThreeSum(3,4,5)