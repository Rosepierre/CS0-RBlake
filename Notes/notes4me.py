import random 
#Seed used for the same random sets
#random.seed("Roger")
#print(random.random()*10)
#print(random.randint(1,10))
#words = ["Apple", "Orange", "Pineapple"]
#print(random.choice(words))
#
#import time
#print(time.localtime())
#
#import string
#print(string.ascii_letters)
#print(string.punctuation)
#print(string.hexdigits)
#letter = "A" 
#print(letter in string.ascii_letters)

#line = input("PLease input two numbers you wish to add (a b)")
#a,b = line.split()

#Last Problem Version two.
#input a name and print hello and goodbye (name) 
#repeat 1 and 2 3 times
#def name_input():
    #name = input() 
    #print(f"Hello and goobye {name}")
#name_input()
#name_input()
#name_input()

import sys

def main():
    
    name_main = input_name()
    answer = solution(name_main)

    print(answer)

def input_name(): 

    name = input()
    return name

def solution(name: str):

    ans = f"Thank you, {name}, and farewell!"
    return ans #passes the answer back onto the calling function
               #our global main program
main()
