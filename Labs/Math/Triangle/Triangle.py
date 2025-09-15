#Roger Blake Triangle Homework 9/15/25
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
s = (a + b + c)/2
s = float(s)
perimeter = (a + b + c)
if(a + b > c) and (a + c > b) and (b + c > a ):
    print("This triangle is real.")
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    #printing the results
    print("The area of the triangle is: ", area)
    print("Semi Perimeter = ", S)
    print("The Perimeter of the triangle is:", perimeter)
    #If statement to determine whether the triangle is real.
else:
    print("This is not a real triangle.")
print({a, b, c,})
#Herons formula for area

