"""
Lab - Playing with Loops
Updated By: Roger Blake
CSCI 110
Date: 9/30/25
Program prints geometric shapes of given height with * using loops
"""
import os
import sys


def printTriangle(height):
    """
    Function takes height as an argument to print the triangle
    of that height with *
    """
    i = 1
    while i <= height:
        print('*  '*i)
        i += 1
    print()  # print an empty line

def printFlippedTriangle(height):
    """
    # Implement the function that takes height as an argument
    # and prints a triangle with * of given height.
    # Triangle of height 5, e.g., should look like the following.
    * * * * *
    * * * *
    * * *
    * *
    *
    """
    i = height
    while i >= 0:
        print('*  ' *i)
        i -= 1

pass


# FIXED
# Design and implement a function that takes a number as height and
# prints square of the given height with *.
# Square of height 5, e.g., would look like the following.
"""
*  *  *  *  *  
*  *  *  *  *   
*  *  *  *  *   
*  *  *  *  *   
*  *  *  *  *   
"""
def square(height):
    i = 1
    while i <= height:
        print('*  '*height)
        i += 1
    print()

def clearScreen():
    """
    function to clear screen based on the operating system
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    # FIXED add a loop to make the program to continue to run until the user wants to quit
    while(True):
            
        # FIXED call clearScreen function to clear the screen for each round of the loop
        clearScreen()
        print('Program prints geometric shapes of given height with *')
        height = int(input('Please enter the height of the shape: '))
        # call printTriangle function passing user entered height
        printTriangle(height)
        

        # FIXED
        # Call printFlippedTriangle passing proper argument
        # Manually test the function
        printFlippedTriangle(height)
        # FIXED
        # Call the function defined in FIXME4 passing proper argument
        # Manually test the function
        square(height)
        # FIXED
        # prompt user to enter y/Y to continue anything else to quit
        exit_q = input("Would you like to continue? ")
        # FIXED
        # Use conditional statements to break the loop or continue in the loop
        if exit_q.lower() != 'y':
            break
            
if __name__ == "__main__":
    main()
