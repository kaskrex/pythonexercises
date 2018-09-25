a = int(input("No. of sides?"))
if a == 3:
    b = input("How many equal sides?")
    if b == 0 or b == 1:
        print("Just a triangle")
    elif b == 2:
        print("Isoceles")
    elif b == 3:
        print("Equilateral")
    else:
        print("Invalid")
    
elif a == 4:
    b = input("How many parallel sides?")
    if b == 2:
        print("Trapezium")
    elif b == 4:
        print("Parallelogram")
    else:
        print("Invalid")

elif a == 5:
    print("Pentagon")
    
elif a == 6:
    print("Hexagon")
    
else:
    print("Invalid")