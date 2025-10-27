#Roger Blake
#Find fbi in multiple lines of text and print which line it is on.
#this will not work for kattis as I could not figure out how to stop the test cases from printing in output, but without the test case it will aways pass

import os

# Clears screen
os.system('cls' if os.name == 'nt' else 'clear')

text = []
for i in range(5):
    lines = input()
    text.append(lines)

def fbi(text):

    fbis = []
    for here in range(len(text)):
        if "fbi" in text[here].lower():
            fbis.append(here + 1)

    if fbis:
        for line in fbis:
            print(f"{line}")
    else:
        print("He got away!")
    return fbis

def test():
    ans = fbi(["aslka;slkfbi", ";alskd;aslkd;", "fbia;ldjqwlkej", "fda;sjlkfdjk;lfds", "fdakjldsfkjew"])
    expected = [1, 3]
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
    
    ans = fbi(["zjksadkdsasad", "zdl;ksdjfbia;lkj", "fbia;ldjqwlkej", "fda;sjlkfbifdjk;lfds", "fdakjldsfkjasl;kjfbiew"])
    expected = [2, 3, 4, 5]
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
    
    ans = fbi(["aslka;sasdjlk", ";asflkjarh66;", "fbia;ldjqwstsrfsalkej", "rsglrkjrteys", "bndkelsrkrnl"])
    expected = [3]
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

    ans = fbi(["aslka;sasdjlk", ";asflkjarh66;", "a;ldjqwstsrfsalkej", "rsglrkjrteys", "bndkelsrkrnl"])
    expected = []
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
    print("Above numbers are the test case answers, test cases have been passed...")

test()
fbi(text)