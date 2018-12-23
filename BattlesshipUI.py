##Battlesship - A curses based multiplayer battleship over ssh game
##2018 Amaia Industries

import curses
from curses import wrapper

def main(stdscr):
	##ALL COORDINATES ARE IN Y(LINE),X(COL) FORMAT!!!!
	stdscr.clear()
	stdscr.addstr(0,0,"Curses is a trick")
	lines = curses.LINES
	stdscr.addstr(1,0,"Lines: " + str(curses.LINES))
	stdscr.addstr(2,0,"COLS: " + str(curses.COLS))
	stdscr.refresh()

	

	gamewin = stdscr.subwin(5,5,5,5)
	gamewin.box()
	gamewin.addstr(1,1,"@")
	gamewin.refresh()
	stdscr.getkey()
wrapper(main)
