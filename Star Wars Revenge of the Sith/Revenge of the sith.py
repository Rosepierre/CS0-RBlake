import curses
import time

# Opening crawl text for Revenge of the Sith
opening = """
Episode III
REVENGE OF THE SITH

War! The Republic is crumbling under attacks by the ruthless
Sith Lord, Count Dooku. There are heroes on both sides.
Evil is everywhere.

In a stunning move, the fiendish droid leader, General Grievous,
has swept into the Republic capital and kidnapped Chancellor
Palpatine, leader of the Galactic Senate.

As the Separatist Droid Army attempts to flee the besieged capital
with their valuable hostage, two Jedi Knights lead a desperate
mission to rescue the captive Chancellor....
"""

def rots_opening(stdscr):
    curses.curs_set(0) #Hides the cursor
    stdscr.clear() #Clears the Screen
    stdscr.nodelay(True) #does not wait for user input
    stdscr.timeout(100) #refreshes every 100 miliseconds

    height, width = stdscr.getmaxyx() #Gets the height and the width of the screen

    # Split and center the text
    lines = opening.strip().split('\n')
    lines = [line.center(80) for line in lines]

    # Position text off the bottom of the screen
    pos_y = height

    while True:
        stdscr.clear()
        for idx, line in enumerate(lines):
            y = pos_y + idx
            if 0 <= y < height:
                x = (width - len(line)) // 2
                stdscr.addstr(y, x, line)
        stdscr.refresh()
        pos_y -= 1

        # Exit when all text has scrolled past the top
        if pos_y + len(lines) < 0:
            break

        time.sleep(1)

    stdscr.addstr(height - 1, 0, "Press any key to exit...")
    stdscr.nodelay(False)
    stdscr.getkey()

if __name__ == "__main__":
    curses.wrapper(rots_opening)