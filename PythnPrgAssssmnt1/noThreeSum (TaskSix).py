def fixThree (n): 
   if n % 3 == 0 and not (n >= 20 and n <= 29): 
      n = 0 
   return n 

def noThreeSum (valA,valB,valC): 
   valA = fixThree(valA)
   valB = fixThree(valB)
   valC = fixThree(valC)
   sum = (valA + valB + valC) 
   return (sum)

noThreeSum(3,4,5)
