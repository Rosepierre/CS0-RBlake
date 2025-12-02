#Lab - Object Oriented Programming (OOP)
#By: Roger Blake

#CSCI 110
#Date: 11/26/25

"""Object Oriented Programming:
Using user-defined class/type, program finds area and 
circumference of a circle.
"""

import math


class Circle(object):
    """
    Class that represents a circle with three attributes – radius, area and circumference.
    Class has two user-defined methods findArea and findCirumference and two special 
    built-in methods:   __init__ and __str__.
    """

    def __init__(self, r=0):
        self.radius = r
        self.area = self.findArea()
        self.circumference = self.findCircumference()

    def findArea(self):
        return math.pi*(self.radius**2)

    def findCircumference(self):
        # FIXED: Find and return the circumference of the circle (20 pts)
        return (2*math.pi*self.radius)

    def __str__(self):
         # FIXED Modify the statement to return circumference as well (20 pts)
        return "Circle - radius: {:.2f}, area: {:.2f}, and circumference: {:.2f}".format(self.radius, self.area, self.circumference)


def main():
    # instantiate aCir object with radius 1
    aCir = Circle(1)
    print(aCir)
    # FIXED (20 pts)
    # Instantiate another circle with radius 5
    aCir2 = Circle(5)
    # Print the circle
    print(aCir2)
    # FIXED: (20 pts)
    # prompt user to enter radius and store into a variable
    radius = int(input("Please enter the radius of your circle: "))
    
    # FIXED (20 pts)
    # create a circle with the user provided radius
    aCir3 = Circle(radius)
    # print the circle
    print(aCir3)


if __name__ == "__main__":
    main()