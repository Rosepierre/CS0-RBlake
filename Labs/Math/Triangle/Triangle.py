#This program will calculate the Area and perimeter of a triangle with 3 given sides as well as determine whether it is a real triangle or not.

#Two imported libraries to use a couple of functions.

#math for the math functions
import math

#time to sleep for the sake of cleaning up the program a bit.
import time

#Introduction to program
print("Welcome to my program, this program is for calculating the Area and the Perimeter of a triangle with 3 given sides as well as finding out if the triangle is even real.")

#sleep function to give time to read the intro before the input.
time.sleep(3)

#storing the input.
sides = input("Please enter 3 sides of the triangle all seperated by spaces: ")
#split the input into seperate variable.
a, b, c =  sides.split()
#floating data to use for math.
a = float(a)
b = float(b)
c = float(c)
S = (a + b + c)/2
S = float(S)
Perimeter = (a + b + c)
print({a, b, c,})
#Herons formula for area
Area = math.sqrt(S*(S-a)*(S-b)*(S-c))
#printing the results
print("The area of the triangle is: ", Area)
print("Semi Perimeter = ", S)
print("The Perimeter of the triangle is:", Perimeter)
#If statement to determine whether the triangle is real.
if(a + b > c) or (a + c > b) or (b + c > a ):
    print("This triangle is real.")
else:
    print("This is not a real triangle.")