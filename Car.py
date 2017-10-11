class car(object):
    """docstring for car."""
    def __init__(self,price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price < 10000:
            self.tax = 0.12
        else:
            self.tax = 0.15


    def display_all(self):
        print "Price: {}".format(self.price)
        print "Speed: {}".format(self.speed)
        print "Fuel: {}".format(self.fuel)
        print "Milage: {}".format(self.mileage)
        print "Tax: {}".format(self.tax)

        return self

car1 = car(2000, "35mph", "Full", "15m")
car2 = car(20000000, "35mph", "Empty", "15m")

print car2.display_all()
