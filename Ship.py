##SHIP.py##
##2018 Amaia Industries

from enum import Enum

class Facing(Enum):
	North = 1
	East = 2
	South = 3
	West = 4

class ship:
	size = 2
	moves = 1
	rotateCost = 0
	facing = Facing.West
	
	
