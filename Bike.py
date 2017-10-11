class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayinfo(self):
        print "This is the price of the bike: {}".format(self.price)
        print "This is the maximun speed this bike can go: {}".format(self.max_speed)
        print "The miles of the bike are: {}".format(self.miles)
        return self

    def ride(self):
        print "Riding..."
        self.miles += 10
        print "The miles of the bike are now {}".format(self.miles)
        return self
    def reverse(self):
        print "Reversing..."
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0
        print "The miles of the bike are now {}".format(self.miles)
        return self

new_bike = Bike(200, "25 mph")
new_bike2 = Bike(200, "25 mph")
new_bike3 = Bike(50000, "25 mph")
""" Bike 1 """
# print new_bike.ride().ride().ride().reverse()
# print new_bike.displayinfo()

""" Bike 2 """
print new_bike2.ride().ride().reverse().reverse()
print new_bike2.displayinfo()

""" Bike 3 """
print new_bike3.reverse().reverse().reverse()
print new_bike3.displayinfo()
