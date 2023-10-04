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
import sys
import math
import config
import vts-rtk as rtk
import vts-network as nw
import vts-status as sts
import vts-layer as layer
import vts-locate as lc
import vts-clean as clean
import vts-lcd as lcd
import flightmanager as fmg

defaultCaste = 1

class vts():
	def __init__(self, pos=rtk.getPos(), caste=defaultCaste, peers=nw.getPeers(), conn=nw.LoRaDataManager(name=f"VTS-{self.caste}"), flightpath=fmg.getFlightPath()):
		self.pos = pos
		self.caste = caste
		self.peers = peers
		self.conn = conn
		self.flightpath = flightpath

	def start(self, objective="groundInit"):
		dead = False
		while not dead:
			match objective:
				case "groundInit":
					if self.conn.checkConnections() and self.conn.getPeerStatus(rt="percent") and rtk.getStatus() == 0 and self.flightpath is not None:
						



if __name__ == "__main__":
	if !config.setup:
		print("Please complete setup before running this file.")
		print("Run \n~/Ventus/config.py\nin a terminal window.")
		sys.exit()
	VTS1 = vts()
	VTS1.start()



