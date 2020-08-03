class Vehicle:
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def my_car(self):
        print("My car is a %d %s %s." % (self.year, self.make, self.model))

car = Vehicle("Volkswagen", "Jetta", 2016)
car.my_car()


