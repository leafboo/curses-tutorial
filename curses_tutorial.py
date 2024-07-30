import curses
from curses import wrapper
import time

def main(stdscr):
  curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_WHITE)
  curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_MAGENTA) # curses.init_pair(id, foreground, background)
  CYAN_AND_WHITE = curses.color_pair(1)
  GREEN_AND_MAGENTA = curses.color_pair(2) # variable names are all caps if it is a constant variable
  

  #stdscr.addstr(0, 10, "hello world", GREEN_AND_MAGENTA | curses.A_UNDERLINE) #  stdscr.addstr(y, x, print_statement)
  for i in range(100):
    stdscr.clear()
    color = CYAN_AND_WHITE

    if i % 2 == 0:
      color = GREEN_AND_MAGENTA

    stdscr.addstr(0, 0, f"Count: {i}", color)
    stdscr.refresh() # send button
    time.sleep(.5)
  stdscr.getch()

wrapper(main)

