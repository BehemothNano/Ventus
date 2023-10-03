!#/usr/bin/python3
"""
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



