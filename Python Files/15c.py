a = "a b c d e fg"
b = ["h", "g", 2, "t"]

#converts string into list
x = a.split(' ')
print(x)

while len(x) != 10:
    #debug
    b = b.pop()
    print("Add", b)
    x.append(b)
    print("Got %d items now" % len(x))

print(" ".join(a))