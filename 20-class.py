class Person:
    def __init__(self, name):
        self.name = name
        self.quote = "test"
    
    def record_quote(self, quote):
        self.quote = quote
        
    def quote(self):
        print("%s said: \"%s\"" % (self.name, self.quote))
            
    def greet(self):
        print("%s says hi" % self.name)

#Init obj called idiot                        
idiot = Person("test")
idiot.record_quote("Decency")
#idiot.quote()