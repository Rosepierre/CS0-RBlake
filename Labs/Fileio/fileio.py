"""
File I/O Lab
By: Roger Blake

CSCI 110
Date: 11/12/25

Program prompts user to enter name of the file that contains 10 integers.
It opens, reads and stores the numbers into a list.
Program will then sort the numbers in the list in ascending and descending orders
Program will then print the sorted lists to an output file along with the 
largest and smallest values in the list.

NOTE: All fixme's are each worth 10 points except for the FIXME1 which is worth 20 points
"""

totalInts = 10


def readData():

    intList = []

    #FIXED (20 points):
    # Prompt user to input file name
    # open the file; read each number one line at a time;
    # and store it into intList list
    # close the file
    # return the intList
    #return intList
    file_name = input("Please enter name of your file: ")

    with open(f'{file_name}', 'r') as fin:
        for line in fin:
            line = line.strip()
            if line:
                intList.append(int(line))
    return intList
    
    

def sortListInAscendingOrder(lstInts):
    # FIXED
     # sort lstInts list in ascending order

    lstInts = lstInts.sort()
   
   

def sortListInDescendingOrder(lstInts):
    # FIXED
    # sort lstInts in descending order

    lstInts = lstInts.sort(reverse=True)
    
    


def printList(printFile, lstInts):
    for i in lstInts:

        # FIXED
        # write each value one line at a time to file
        # handled by printFile object.

        printFile.write(f'{i}\n')


def main():
    integers = []  # list to store integers
    integers = readData()
    outputFileName = input('Enter a file to write output to: ')
    printFile = open(outputFileName, 'w')
    printFile.write("Numbers entered:\n")
    printList(printFile, integers)
    # sort numbers
    sortListInAscendingOrder(integers)
    printFile.write("Numbers sorted in ascending order:\n")
    printList(printFile, integers)

    # FIXED
    # Call sortListInDescendingOrder function
    sortListInDescendingOrder(integers)

    # FIXED
    # Write the sorted list in descending order to the output file

    printFile.write("Numbers sorted in descending order:\n")
    printList(printFile, integers)

    # FIXED
    # Print the largest number to the output file

    printFile.write("Largest number is:\n")
    printFile.write(str(max(integers)) + "\n")

    # FIXED
    # Print the smallest number to the output file
    
    printFile.write("Smallest number is:\n")
    printFile.write(str(min(integers)))
    printFile.close()
    print('Done executing the program! Check the output file for results.')


# FIXED
# Call main function if this module is run as the main module

if __name__ == "__main__":
    main()