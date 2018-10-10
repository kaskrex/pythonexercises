class GiftReceiver:
    
    def __init__(self, name, starting_gift_count=0):
        print("Creating a GiftReceiver %s." % name)
        self.name = name
        self.starting_gift_count = starting_gift_count
        self.gifts_received = 0 # by default no gifts are received in the beginning
        self.gifts_given = 0
        # an attribute that is derived from another attribute
        self.current_gift_count = self.starting_gift_count
        
    def receive(self, number=1):
        self.gifts_received += number
        self.current_gift_count += number
        
    def give(self, number=1):
        # more flexibility when you return True or False instead of printing or doing some function
        if number > self.current_gift_count:
            return False
        else:
            self.gifts_given += number
            self.current_gift_count -= number
            return True
        
    def print_information(self):
        print("")
        print("-" * 40)
        print("%s started with %d gift(s)." % (self.name, self.starting_gift_count))
        print("He has received %d gift(s)." % self.gifts_received)
        print("He has given %d gift(s)." % self.gifts_given)
        print("He currently has %d gift(s)." % (self.current_gift_count))
        print("-" * 40)
        
giver_1 = GiftReceiver("Bob", 0)
giver_1.receive()
giver_1.receive(2)

if giver_1.give(4):
    print("%s has given %d gifts!" % (giver_1.name, number))
else:
    print("%s does not have any more gifts to give. He currently has %d!"% (giver_1.name, giver_1.current_gift_count))

giver_2 = GiftReceiver("Tom", 2)

giver_1.print_information()
giver_2.print_information() 