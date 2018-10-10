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
            print("%s said: \"%s\"" % (self.name, quote))        
            
    def greet(self):
        print("%s says hi" % self.name)

a = Person("a")
a.greet()
a.record_quote("x")
a.record_quote("y")
a.record_quote("z")
a.all()