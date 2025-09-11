#accepted: 0
#cpu_limit: 1 second
#difficulty: 1.2 Easy
#mem_limit: 1024 MB
#problemid: addtwonumbers
#submissions: 0
#title: Add Two Numbers

"""
Math and Variables Lab
By: Roger Blake
CSCI 110 Lab
Date: 9/9/25
 
Read and solve: Add Two Numbers - https://open.kattis.com/problems/addtwonumbers 
 
Algorithm steps:
  1. Read data as a line
  2. Split the line into two integers
  3. Add them up
  4. print the result
"""

import sys


def main():
    line = input("Please enter the two numbers you wish to add: ")
    # split the data into two numbers
    a, b = line.split()
    # check to see if the data is split correctly
    print(f'{a=}, {b=}', file=sys.stderr)
    # FIXED 2: convert string a into integer
    a = int(a)
    # FIXED 3: convert string b into integer
    b = int(b)
    # FIXME 4: add two numbers and store the result into ans variable
    result = (a + b)

    # FIXME 5: print the answer as shown in the sample output
    print(result)

    """Main function that solves the problem
    """

    # FIXME1 - read input data into a variable #fixed#
    

main()  # call main function
