class Vehicle:
    def __init__(self, make, colour):
        self.make = make
        self.colour = colour

    def driving(self):
        self.drive = 4

class Motorcycle(Vehicle):
    def driving(self):
        self.drive = 2

class Bike(Vehicle):
    def __init__(self, make, colour, cool_factor):
        super.__init__(make, colour)
        self.cool_factor = cool_factor

