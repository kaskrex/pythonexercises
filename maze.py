a = input("Choose between 2 doors")
if a == str(1):
    print("Door #1 choosen")
    
elif a == str(2):
    print("Door #2 choosen")
    
else:
    print("Wrong door! Choose again!")
    #if r = 1, restart counter
    r = 1
    
    while r == 1:
        a = input("Choose between 2 doors")
        if a == str(1):
            print("Door #1 choosen")
            
            b = input("Saw a bear, run or yell?")
            if b == "run":
                print("Which path do you take?")
                    
            elif b == "yell":
                print("Sore throat no voice")
            
            else: 
                print("Die only, but heaven doesn't want you. Try again!")
                r = 1
                
                while r == 1:
                    b = input("Saw a bear, run or yell?")
                    if b == "run":
                        print("Which path do you take?")
                        r = 0
                            
                    elif b == "yell":
                        print("Sore throat no voice")
                        r = 0
                    
                    else: 
                        print("Die only, but heaven doesn't want you. Try again!")
                        r = 1
                    
                
            
        elif a == str(2):
            print("Door #2 choosen")
            r = 0
                