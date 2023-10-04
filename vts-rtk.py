!#/usr/bin/python3
"""
Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
Neither the name of the University nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED ''AS IS'' AND WITHOUT ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, WITHOUT LIMITATION, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

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
