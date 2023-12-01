#!/usr/bin/python3
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
import skutils as sku
# import vts-network as nw

# Ensure these are correct before running, also not recommended to run this over insecure/public networks
# Note: incrementing the base port fixes 
serverIP = '10.11.2.60'
basePort = 10002
usedPorts = [basePort]

def bInput(prompt):
    """
    Converts user's input to bytes, if msg == quit, just returns 'quit'.
    """
    while True:
        userInput = input(prompt)
        if userInput != "" and userInput != "quit":
            return userInput.encode('utf-8')
        elif userInput == "quit":
            return "quit"

def assignPort():
    port = usedPorts[-1] + 1
    usedPorts.append(port)
    return port

def receive(sk):
    connection, ca = sk.accept()
    while True:
        data = connection.recv(1024).decode('utf-8')
        if not data:
            break
        connection.send(data)
    connection.close()
    return data



def setup():
    # Create a TCP/IP socket
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addresses = [(serverIP, basePort)]
    server_address = (serverIP, basePort) # Server's local IP, port
    print(f"{sys.stderr}\nStarting up on {serverIP} with port {basePort} -- connect to {serverIP}:{basePort} for port assignment.")
    sk.bind(server_address)
    sk.listen(1)
    connections = {}
    while True:
        # Big comment 1 (see below)
        # Stuff prior to tick (not really obviously, just helps for thinking about it)
        connection, clientAddress = sk.accept()
        if connection not in connections:
            pt = assignPort() # Get port assignment
            sk.sendall(pt.encode('utf-8')) # Send port assignment
            sk.bind((serverIP, pt)) # Switch to new port
            sk.listen(1)
            if receive(connection) == "connected":
                # append connection to dict after checking if it's a new connection (need to fix, this will append the connection to the port assignment port)
                connections[clientAddress] = [connection, pt] # Store port client is connected to server on to allow future reconnects
                print(f"INFO: Established connection to client at {clientAddress}")
            else:
                print(f"WARN: Failed to establish connection to new client at {clientAddress}.")
            sk.bind((serverIP, basePort)) # Revert to connection request port
            sk.listen(1)
        
        print(f"--------------\nCurrent connections: {connections}\n----\nNumber of connections: {len(connections)}\n--------------")
        # Stuff that happens in tick
        try:
            # data/tick, not anything to do with tickets if at all unclear
            tickData = {}
            clientPorts = [connections[clientAddress][1] for clientAddress in connections] # List of ports
            """
            Port to CA:
            clientPorts - a list of ports unassociated with their owners (respective clients)
            

            """
            for pt in clientPorts:
                # Format: CA: connection, port client is connected to
                sk.bind((serverIP, pt))
                sk.listen(1)
                sku.send("connected")
                # Behavior of receive is a bit questionable, test to ensure it only gets one item, or if multiple, all items instead of just last.
                clientData = sku.receive(sk) 
                # Generate tick data by adding data from each client to the tickData dict
                tickData[clientAddress] = clientData # Tick data will be fully generated after this for loop, see below.
            # Do something w/ tick data here (it's complete now)
            print(f"-------\nData: {tickData}\n-------")
            # Set up to stop server if certain message from user is received
            if tickData["ui"] == "end":
                break

        except:
            print("WARN: Unable to gather tick data.")
            connection.close() # ?
    sk.close()
    return 0

if __name__ == "__main__":
    stp = setup()
    if stp == 0:
        # do other stuff
        print("Client setup complete.")
    else:
        print(f"FATAL: Unable to complete setup - {stp}")




"""
Relocated large comments & misc old things:

Big Comment 1:
IMPORTANT: this will only append to the dict connections. We want this as otherwise the connections 
dict has to be completely regenerated each tick, which isn't possible due to its implementation.
However, it does not handle client disconnects, and clients will still be considered each tick for a message.
This isn't necessarily a bad thing, but errors could arise if a client has disconnected but a recipient is still expecting something.
Find connections - also note that only one client can be discovered/tick


Miscellaneous:
# tickData = {clientAddress: connection.recv(999) for clientAddress, connection in connections} # Format: CA: message
# data = connection.recv(999)
# print(f"Data from latest connection: {data}")

"""