"""
    StdIO Lab
    ASCII Art - using literals and variables
    
    Updated By: <Roger Blake> #Fixed
    Date: 8/26/25 #Fixed
    
    This program produces an ASCII art on the console.

    Algorithm steps: 
    1. Use variables to store data/values
    2. Write a series of print statements to print the data/values to the console
"""

print("Welcome to ASCII Art Program...")

# Fixed: prompt user to enter their name and store the value into name variable using input function
name: str = input("What is your name? [First] ") 
# Fixed: greet the name using the variable as the following output
print("Nice meeting you,", name) 
# must output: Nice meeting you, <name>!

# prompt user to enter the semester and store the value into semester variable using input function
semester: str = input("What semester is this [Fall/Spring]? ") 
print("This is " + semester + " semester.\n")

# Fixed: prompt user to enter the year and store the value into year variable using input function
year: str = input("What year is it? ") 

# Fixed: print the year using the variable as the following output
print("This year is", year ,"year")
# must output: This is <year> year.

print("Hope you like my ASCII art...\n\n")

line1 = "  |\\_/|   **********************     (\\_/)"
print(line1)
line2 = " / @ @ \\  *     ASCII LAB      *    (='v'=)"
print(line2)
line3 = "( <  0 >) *       " + name + "        *    (\")_(\") "
print(line3)
line4 = "  >>x<<   *     "+ semester + " "+ year +"      *"
print(line4)
line5 = " /  O  \\  *      CSCI 111      *"
print(line5)
line6 = "          **********************"
print(line6)
#Darth Vader from https://www.asciiart.eu/movies/star-wars
print("                       .-.")
print("                      |_:_|")
print("                     /(_Y_)\\")
print(".                   ( \\/M\\/ )")
print(" '.               _.'-/'-'\\-'._")
print("   ':           _/.--'[[[[]'--.\\_")
print("     ':        /_'  : |::\"| :  '.\\")
print("       ':     //   ./ |oUU| \\.'  :\\")
print("         ':  _:'..' \\_|___|_/ :   :|")
print("           ':.  .'  |_[___]_|  :.':\\")
print("            [::\\ |  :  | |  :   ; : \\")
print("             '-'   \\/'.| |.' \\  .;.' |")
print("             |\\_    \\  '-'   :       |")
print("             |  \\    \\ .:    :   |   |")
print("             |   \\    | '.   :    \\  |")
print("             /       \\   :. .;       |")
print("            /     |   |  :__/     :  \\\\")
print("           |  |   |    \\:   | \\   |   ||")
print("          /    \\  : :  |:   /  |__|   /|")
print("          |     : : :_/_|  /'._\\  '--|_\\")
print("          /___.-/_|-'   \\  \\")
print("                         '-'             ")
                    
# Fixed: use variable to print the second line of the graphic
# Fixed: print the third line of the graphics
# Fixed: use variable to print the fourth line
# Fixed: line
# Note: You can add more lines oruse variable to print the fifth print more ASCII arts of your choice if you'd like...

print("\nGood bye...  \n")
