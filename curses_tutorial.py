import curses
from curses import wrapper

def main(stdscr):
  stdscr.clear()

  stdscr.addstr(0, 10, "hello world") #  stdscr.addstr(y, x, print_statement)
  print("goodbye")

  stdscr.refresh() # send button
  stdscr.getch()

wrapper(main)

