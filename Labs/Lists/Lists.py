"""
CSCI 110
List Lab

By: Roger Blake
Date: 10/28/25

Program prompts user to enter 10 integers and stores the entered numbers into a list.
Program will then sort the numbers in the list in ascending and descending orders
and print the largest and smallest values in the list.
Program will also print the indices of the largest and smallest numbers in the list.
"""
import os

os.system("cls" if os.name == "nt" else "clear")

totalInts = 10


def getIntegers():
    intList = []
    i = 0
    while i < totalInts:
        num = int(input("Enter an integer: "))
        # FIXED add num into integers list
        intList.append(num)
        i += 1
    return intList


def sortListInAscendingOrder(intList):
    intList.sort()


def sortListInDescendingOrder(intList):
    # FIXED (20 points)
    intList.reverse()
    


def printList(intList):
    for val in intList:
        print(val, end=' ')
    print()


def main():
    integers = []  # empty list to store integers
    integers = getIntegers()
    print("Numbers entered are: ")
    printList(integers)
    print()
    # sort numbers
    sortListInAscendingOrder(integers)
    print("Numbers in ascending order: ")
    printList(integers)
    # FIXED (10 points)
    # Call sortListInDescendingOrder function
    sortListInDescendingOrder(integers)
    # FIXED (10 points)
    # Print the sorted list in descending order
    print(f"Numbers in decending order:")
    printList(integers)
    # FIXED (10 points)
    # Print the largest number
    print(f"The Largest number is: {integers[0]}")
    # FIXED (10 points)
    # Print the smallest number
    print(f"The smallest number is: {integers[-1]}")
    # FIXED (10 points)
    # Find and print the index of the smallest number
    print(f"The index of the smallest number is: {integers.index(integers[-1])}")
    # FIXED (10 points)
    # Print the index of the largest number
    print(f"The index of the largest number is: {integers.index(integers[0])}")


# FIXED (20 points)
# Call main function if this file is run as the main module
if __name__ == "__main__":
    main()
print('call main() function to see partial outputs of the program...')
