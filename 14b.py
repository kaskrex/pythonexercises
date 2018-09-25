a = []

h = 1
f = 2
g = 3

b = [h, f, g]
print(b)

c = [1, "a", 2]
print(c)

#range(x, y, z)
#x = number it starts at
#y = number it ends at 
#z = amount that it increments by

for i in range (2, 11, 3):
    print("Add %d to the list" % i)
    #append range number to list
    a.append(i)

for x in c:
    #type returns object's type
    print(type(x))
    print("%r" % x)
