a = input("School? ")

c = input("Class? ")

e = input("Name? ")

g = input("Math score? ")
h = int(g)
x = int(h)

i = input("Science score? ")
j = int(i)
y = int(j)

k = input("English score? ")
l = int(k)
z = int(l)

if (x < 0) or (x > 100):
    print("Score cannot be negative")

elif (y < 0) or (y > 100):
    print("Score cannot be negative")
    
elif (z < 0) or (z > 100):
    print("Score cannot be negative")
    
else:
    total = x + y + z

    print("School: %s\t" %(a)) 
    print("Class:  %s \t" %(c)) 
    print("\t\t %s\t" %(e)) 
    print("Math\t\t | \t %d/100" %(x))
    print("Science\t\t | \t %d/100" %(y)) 
    print("English\t\t | \t %d/100" %(z))
    
    print("Total Score\t |\t", total, "/300")
