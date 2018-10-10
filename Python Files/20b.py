import random

class Person:
    def __init__(self, name):
        self.name = name
        self.quotes = []
    
    def record_quote(self, quote):
        self.quotes.append(quote)
        
    def quote(self):
        print("%s said: \"%s\"" % (self.name, self.quote))
            
    def all(self):
        for quote in self.quotes:
            print("%s said: \"%s\"" % (self.name, self.quote))        
            
    def speak(self):
        print("%s says %s" % (self.name, random.choice(self.quotes)))
        
    def greet(self):
        print("%s says hi" % self.name)

a = Person("a")
for i in ["a", "b", "c"]:
    a.record_quote(i)
    
a.speak()