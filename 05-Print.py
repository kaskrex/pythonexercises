h = 6
w = 5
a = 23.1
hci = "black"
n = "test"

#%s: string
#%d: number (digit)
#%f: floating numbers (%.xf where x is the number of sf)

print("Hi my \nname is %s. \tMy height is %dcm, weight is %dkg." %(n, h, w))
print("Height: %d. Weight: %dkg, Age: %.2f years old." %(h, w, a))

#print multiple lines in terminal

print("""
eh 
help la

""" + str(h) + str(h) + str(h))

print(hci)
print("List:\n\tone\n\ttwo\n\tthree")