# PythonAssessmentOne
The 1st assessment for my programming fundamentals module - 1st year of Uni.

Below is a list of what the six tasks were and what they do:
  1. Write a function called “str_abba” without arguments, ask the user to enter two
strings, a and b, return the result of putting them together in the order abba, e.g.
"Hi" and "Bye" displays "HiByeByeHi"; “Yo” and “Alice” gives
“YoAliceAliceYo”. 


  2. Write a function called “compare_ages” without arguments that asks for the
user’s age and responds by saying whether the user is the same age as you, younger
or older (and by how much). For example, if you are 18 years old the program
should output the following:
• “You are younger than me by 1 year(s).” (if input is 17)
• “You are the same age as me.” (if input is 18)
• “You are older than me by 2 year(s).” 

  3. Write a function called “guessing_game” without arguments that generates a
random number between 1 and 100, inclusive. Ask the user to guess the number in
a loop until they get it right, advising whether the number is too big or too small.
You should also keep track of the number of guesses the user has made. The
function should output the following:
• That’s not right, g is too small/big (if wrong, where g is the guess)
• That’s right! You took n guess(es) (if correct, where n is the number of guesses).
For this task, you can import and use ‘random.randint’. 

  4. Write a function called “pig_latin” that takes a string input, translates it into
pig latin, and returns the result as a new string. Pig latin is based on the Englishlanguage, where each word is changed such that the first letter is moved to the end
of the word, followed by the letters “ay”. Here is an example:
“This assignment is really bizarre”
becomes
“histay ssignmentaay siay eallyray izarrebay”
Some important things to consider:
• Words should be split by space
• Don’t worry about preserving capitalisation
• You can assume there is no punctuation; just letters and spaces 


Stretch Exercise
  5. Write a function called “cal_frequency” to calculate the frequency of each letter of
the alphabet (i.e. no other characters or whitespaces) in a string of text. The input
string is provided by the user. The function sorts the letters from the most frequent
to the least and displays their corresponding frequencies. Note the function should
return nothing but print each letter and its corresponding frequency, in descending
order. Treat upper and lower case characters of the same letter as being identical
(e.g. a exists in Anna twice, not once; A exists in Anna twice, not once) 

  6. Write a function called “no_three_sum”, which take three integer values a b c as
arguments and returns their sum. However, if any of the values is a multiple of
three e.g. 3, 6, 9, 12, … -- then that value counts as 0, except the multiples of three
between 20 and 29. Write a separate helper function "def fix_three(n):"that takes in
an int value and returns that value fixed for the rule. Then make use of this helper
function through “no_three_sum”. For example,
no_three_sum(1, 2, 3) → 3
no_three_sum(2, 13, 1) → 16
no_three_sum(2, 1, 21) → 24 
