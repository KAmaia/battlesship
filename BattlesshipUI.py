##Battlesship - A curses based multiplayer battleship over ssh game
##2018 Amaia Industries

import curses
from curses import wrapper

def checkSize(screen):
	if screen.getmaxyx()[0] < 24 or screen.getmaxyx()[1] < 80:
		return 1
	else:
		return 0
def main(stdscr):
	##Check to see if the screen we have is big enough for the entire window.  
	##Ideally 80x25
	##If Not Return A Screen Not Big Enough Error, and terminate the session.
	##If So, go to game Lobby.
	validTerminal = checkSize(stdscr)	

	if validTerminal == 0:
		
		curses.curs_set(0)
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

	elif validTerminal == 1:
		stdscr.clear()
		stdscr.addstr(0,0,"Sorry, Your Terminal Must Be At Least 80x25 to play")
		stdscr.refresh()
	stdscr.getkey()
##Wrapper##
wrapper(main)
