test = [1, 2 ,3, 4, 5]
fruit = ["a", "b", "c", "d"]


#prints first item in list
print(test[0])

#prints the whole list
print(test)
print(fruit)

#forloop
for i in test:
    #prints the items in the list sequentially
    print(i)
    count = 0

for x in fruit:
    print(count)
    print(fruit)
    count += 1
    print(count)

#splicing
print(test[0:2])