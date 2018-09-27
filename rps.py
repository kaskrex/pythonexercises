#rock = 1
#paper = 2
#scissors = 3
print("rock = 1")
print("paper = 2")
print("scissors = 3")
x = input("Player 1 choice: ")
y = input("Player 2 choice: ")

a = int(x)
b = int(y)

#r = repeat
r = 0

#while = 1:
if a == 1:
    if b == 1:
        print("Draw")

    elif b == 2:
        print("Player 2 wins!")
    
    elif b == 3:
        print("Player 1 wins!")
    
    else:
        print("Invalid!")

elif a == 2:
    if b == 1:
        print("Player 1 wins!")

    elif b == 2:
        print("Draw")
    
    elif b == 3:
        print("Player 2 wins!")
    
    else:
        print("Invalid!")

elif a == 3:
    if b == 1:
        print("Player 2 wins!")

    elif b == 2:
        print("Draw")
    
    elif b == 3:
        print("Player 1 wins!")
    
    else:
        print("Invalid!")

else:
    print("Invalid! Try Again.")
    r = 0
    
