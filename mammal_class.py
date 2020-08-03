class Mammal:
    def __init__(self, name, type_of_mammal, breed, legs):
        self.type_of_mammal = type_of_mammal
        self.name = name
        self.breed = breed
        self.legs = legs

    def eat(self):
        return "The %s is eating" % (self.type_of_mammal)

class Cat(Mammal):
    def __init__(self, name, type_of_mammal, breed, legs, fur):
        super().__init__(name, type_of_mammal, breed, legs) #Benefit of this will become obvious later
        self.fur = fur #Unique to Cat

    def __str__(self):
        return "%s is a %s %s breed with a %d legs and %s fur." % (self.name, self.breed, self.type_of_mammal, self.legs, self.fur)

    def purr(self):
        return "%s is purring" % (self.name)

    def eat(self):
        return "THE CAT EATS DIFFERENTLY FOR REASONS"
        #YOU CAN OVERRIDE A METHOD FROM YOUR PARENT IN THE SUBCLASS

guster = Cat("Gus", "cat", "mixed", 4, "short hair")
harry = Mammal("Harry", "dog", "bischon frize", 4)
print(guster)
print(guster.eat())
print(harry.eat) #DESIGNED TO FAIL