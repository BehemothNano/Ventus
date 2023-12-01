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
import socket
import sys
import vts-lora as LoRa

class LoRaDataManager():
    def __init__(self, name, freq = None, mode = "aerial"):
        self.name = name
        if self.freq is not None:
            self.freq = freq
        else:
            self.freq = LoRa.getFreq()
        self.mode = mode
        self.received = {}

    def send(self, data, dataType, intent encryption = True, targets = "all", timeout = 3000, expiration = None, requireResponse = False):
        
    
    def getDataByID(self, dataID):
        return self.received.get(dataID)
    
    def dump(self):
        print(f"{self.received.id}: {self.received}") for i in self.received
    
    def rmData(self, targetIDs):
        for target in targetIDs:
            self.received.drop(target)
        return True

