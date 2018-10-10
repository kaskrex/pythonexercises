g = input("Height in m? ")
x = float(g)
z = x ** 2

i = input("Weight in kg/? ")
y = int(i)


def bmi(z, y):
    cal = y/z
    return cal
    
#print(z)

res = bmi(z, y)
print(res)

if (res < 18.5) or (res >= 0):
    print("Underweight")

elif (res >= 18.5) or (res < 24.9):
    print("Normal")
    
elif (res >= 24.9) or (res < 29.9):
    print("Overweight")
    
else:
    print("Extra fat")

