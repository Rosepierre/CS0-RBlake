#Roger Blake
#Program to solve the New Alphabet kattis problem

import os

# Clears screen
os.system('cls' if os.name == 'nt' else 'clear')

newalpha = {'a' : "@", 'b' : "8", 'c':"(", 'd':"|)", 'e':"3", 'f':"#", 'g':"6", 'h':"[-]", 'i':"|", 'j':"_|", 'k':"|<", 'l':"1", 'm':"[]\/[]", 'n':"[]\[]", 'o':"0", 'p':"|D", 'q':"(,)", 'r':"|Z", 's':"$", 't':"']['", 'u':"|_|", 'v':"\/", 'w':"\/\/", 'x':"}{", 'y':"`/", 'z':"2"}

#grabs in input

def main(wordstoreplace):

    #will endup the translation
    fix = ""

    wordstoreplace = wordstoreplace.lower()

    #for loop to go through each letter
    for char in wordstoreplace:
        fix += newalpha.get(char, char)

    print(f"{fix}")

    return fix

def test():
     ans = main("A")
     expected = "@"
     assert ans == expected, f"Expected: {expected}, but got: {ans}"
     print("All test cases passed!")

     ans = main("Hello, World!")
     expected = "[-]3110, \/\/0|Z1|)!"
     assert ans == expected, f"Expected: {expected}, but got: {ans}"
     print("All test cases passed!")

     

if __name__ == "__main__":
    test()
    wordstoreplace = input()
    main(wordstoreplace)

