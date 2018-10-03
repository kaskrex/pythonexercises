#generate random number between 0 to 100
#print(random.randint(0, 100))

#random pick
#test = [1, 2, "huh"]
#print(test)
#print(random.choice(test))

#shuffle list
#print(random.shuffle(test))

import itertools
import string
import random 
import nltk

foo = "aaasssc"

#choose length of password
#a = input(int("Enter number"))

#list of characters
#x = []
x = string.ascii_uppercase
x = [x[i] for i in range(0, len(x), 1)]
print(x)

y = []
y = string.ascii_lowercase 
y = [y[i] for i in range(0, len(y), 1)]
print(y)

z = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(z)



#removes repeated characters
#b = ''.join(ch for ch, _ in itertools.groupby(b))
#print(b)