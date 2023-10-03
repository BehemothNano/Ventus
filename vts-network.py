!#/usr/bin/python3
"""
Using the MIT License. (C) 2023 Dylan Buchanan
"""
import os
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
        pass
    
    def getDataByID(self, dataID):
        return self.received.get(dataID)
    
    def dump(self):
        print(f"{self.received.id}: {self.received}") for i in self.received
    
    def rmData(self, targetIDs):
        for target in targetIDs:
            self.received.drop(target)
        return True

