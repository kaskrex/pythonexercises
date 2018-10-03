#generate random number between 0 to 100
#print(random.randint(0, 100))

#random pick
#test = [1, 2, "huh"]
#print(test)
#print(random.choice(test))

#shuffle list
#print(random.shuffle(test))

# 1. User choose pw len
# 3. Use for loop that loops for pwlen-1 (?) to push in characters randomly picked at each iteration
# 4. Once a character has been picked, pop that character from original list 

import itertools
import string
import random 
import nltk

#choose length of password
pwlen = int(input("Enter number"))

#list of characters
x = string.ascii_uppercase
x = [x[i] for i in range(0, len(x), 1)]

y = string.ascii_lowercase 
y = [y[i] for i in range(0, len(y), 1)]

z = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#List of all possible characters 
fin = x + y + z

#Empty list that'll contain final list
pw = []

for i in range(pwlen):

    #choose character from list at random
    chose = random.choice(fin)
    
    #locate position of chosen character from index
    pos = fin.index(chose)
    
    #convert to type string
    chosen = str(chose)
    
    #append chosen character to list
    pw.append(chosen)
    
    #pop chosen character from list
    fin.pop(pos)
    
strpw = ''.join(pw)
print("Password is: ", strpw)