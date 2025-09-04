"""
    StdIO Lab 1B
    ASCII Art 2 - using literals and variables
    
    Updated By: <Roger Blake> #FIXED
    Date: 9/2/2025 ##Fixed
    
    This program produces an ASCII art on the console.
    It should look something like this.


         /\         ************************************************************      /~~   ~~\
        /##\                                                                       /~~         ~~\
       /#""#\                               Ascii Art 2                           {               }
      /#"##"#\                                 CS110                               \  _-     -_  /
     /#"#""#"#\                              Spring 25                              ~  \\   //  ~
    /#"#CMU!#"#\                            Corin Chepko                          _- -   | | _- _
         ||                                                                         _ -  | |   -_
         ||         ************************************************************        // \\

    Algorithm steps: 
    1. Use variables to store art and data
    2. Write a series of print statements to print the data/values to the console, using the .center() method
        to keep the strings centered.
    
    Note: You can add more lines or print differt ASCII arts of your choice if you'd like...
"""

print("Welcome to ASCII Art Program...\n")

# FIXED: prompt user to enter their name and store the value into name variable using input function
name = input("Please enter your first and last name ")
# FIXED: greet the name using the variable as the following output
print("Nice meeting you,", name,".")
# must output: Nice meeting you, <name>!

# prompt user to enter the semester and store the value into semester variable using input function
semester: str = input("What semester is this [Fall/Spring]? ")

# FIXED: prompt user to enter the course name and store the value into a variable using input function
course_name = input("What course is this? ")

# FIXED: prompt user to enter the lab title and store the value into a variable using input function
lab_title = input("What is the name of this lab? ")

print("Hope you like my ASCII art...\n\n")

# construct the art using set of three strings, one for art on the left, 
# one for the center text, and one for the art on the right
# We use 16 spaces for each art column and 30 spaces for the text in the center and border
left_width = 20
right_width = 20
center_width = 40  # Can change for smaller screens

# The extra spaces are not nessesary, but I used them to help line up the art
treeA_1: str = "      /\\     "
treeA_2: str = "     /##\\    "
treeA_3 = '''/#""#\\'''
treeA_4 = '''/#"##"#\\'''
treeA_5 = '''/#"#""#"#\\'''
treeA_6 = '''/#"#CMU!#"#\\'''
treeA_7 = "||"
treeA_8 = "||"

treeB_1: str = "   /~~   ~~\\  "
treeB_2: str = "  /~~         ~~\\"
treeB_3 =      " {               }"
treeB_4 =  " \  _-     -_  /"
treeB_5 = "  ~  \\\   //  ~"
treeB_6 = "_- -   | | _- _"
treeB_7 = "  _ -  | |   -_"
treeB_8 = "  // \\\ "

# Fixed7-8: use variables to add the rest of the art # I DID IT ABOVE THIS

asterics: str = "*"*center_width
spaces: str = " "*center_width

print(treeA_1.center(left_width) + asterics.center(center_width) + treeB_1.center(right_width))
print(treeA_2.center(left_width) + spaces.center(center_width) + treeB_2.center(right_width))
print(treeA_3.center(left_width) + lab_title.center(center_width) + treeB_3.center(right_width))
print(treeA_4.center(left_width) + course_name.center(center_width) + treeB_4.center(right_width))
print(treeA_5.center(left_width) + semester.center(center_width) + treeB_5.center(right_width))
print(treeA_6.center(left_width) + name.center(center_width) + treeB_6.center(right_width))
print(treeA_7.center(left_width) + spaces.center(center_width) + treeB_7.center(right_width))
print(treeA_8.center(left_width) + asterics.center(center_width)+ treeB_8.center(right_width))


# # FIXED9-10: print the rest of the art, including the collected name, lab title, course, and semester
# # Note: You can add more lines or print differt ASCII arts of your choice if you'd like...


yes_no = input("Would you like to proceed? It may be a trap.\n")
while yes_no.lower() != 'yes' and yes_no.lower()!= 'no':
    yes_no = input("Yes or no please. ")
if yes_no.lower() == 'yes':
    #Art from https://www.asciiart.eu/movies/star-wars
    print('''                            __...------------._
                         ,-'                   `-.
                      ,-'                         `.
                    ,'                            ,-`.
                   ;                              `-' `.
                  ;                                 .-. \\
                 ;                           .-.    `-'  \\
                ;                            `-'          \\
               ;                                          `.
               ;                                           :
              ;                                            |
             ;                                             ;
            ;                            ___              ;
           ;                        ,-;-','.`.__          |
       _..;                      ,-' ;`,'.`,'.--`.        |
      ///;           ,-'   `. ,-'   ;` ;`,','_.--=:      /
     |'':          ,'        :     ;` ;,;,,-'_.-._`.   ,'
     '  :         ;_.-.      `.    :' ;;;'.ee.    \\|  /
      \\.'    _..-'/8o. `.     :    :! ' ':8888)   || /
       ||`-''    \\\\88o\\ :     :    :! :  :`""'    ;;/
       ||         \\"88o\\;     `.    \\ `. `.      ;,'
       /)   ___    `."'/(--.._ `.    `.`.  `-..-' ;--.
       \\(.="""""==.. `'-'     `.|      `-`-..__.-' `. `.
        |          `"==.__      )                    )  ;
        |   ||           `"=== '                   .'  .'
        /\\,,||||  | |           \\                .'   .'
        | |||'|' |'|'           \\|             .'   _.' \\
        | |\\' |  |           || ||           .'    .'    \\
        ' | \\ ' |'  .   ``-- `| ||         .'    .'       \\
          '  |  ' |  .    ``-.._ |  ;    .'    .'          `.
       _.--,;`.       .  --  ...._,'   .'    .'              `.__
     ,'  ,';   `.     .   --..__..--'.'    .'                __/_\\
   ,'   ; ;     |    .   --..__.._.'     .'                ,'     `.
  /    ; :     ;     .    -.. _.'     _.'                 /         `
 /     :  `-._ |    .    _.--'     _.'                   |
/       `.    `--....--''       _.'                      |
          `._              _..-'                         |
             `-..____...-''                              |
                                                         |
                               mGk                       | ''')
elif yes_no.lower() == 'no':
    print('''
        .---. 
      .'_:___".
      |__ --==|
      [  ]  :[|
      |__| I=[|
      / / ____|
     |-/.____.'
snd /___\\ /___\\
''')

print("\n Good bye...  \n")
