!#/usr/bin/python3
"""
Using the MIT License. (C) 2023 Dylan Buchanan
"""
import os
import math
import pickle

home = []

def getPos():
	pos = rtk.pos
	return pos

def getHeading():
	heading = rtk.head
	return heading

def getDistToHome():
	dlX = math.abs(home[0] - )
	dlZ = math.abs(home[1] - )
	dist = (math.sqrt((dlX ** 2) + (dlZ ** 2)))
	return dist
