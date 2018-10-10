x = {
    "name": "a",
    "age": 29,
    "height": 198,
    "math": 10*10+50
}

print(x["name"])
print(x["age"])
print(x["height"])
print(x["math"])

#Add new key-value pair to dictionary
x["loc"] = "SG"

states = {
    "Oregon": "OR",
    "Florida": "FL",
    "California": "CA",
    "New York": "NY"
}

cities = {
    "CA": "San Fransico",
    "FL": "Jacksonville",
    "NY": "New York",
    "OR:": "Portland"
}

print(states)
print(cities)

#debug: keyerror
print("Oregon is %s, its city is %s" % (states["Oregon"], states[cities["OR"]]))