#!/usr/bin/python3
"""
Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
Neither the name of the University nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED ''AS IS'' AND WITHOUT ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, WITHOUT LIMITATION, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

Using the MIT License. (C) 2023 Dylan Buchanan
"""
import socket
import sys
import time
import skutils as sku

serverIP = '10.11.2.60'
serverPort = 10002

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


def testLatency(clientID):
    t1_client = time.time()
    sk.sendall(f"Latency test | CID: {clientID}".encode('utf-8'))

def request(sk, itemID):
    """ 
    To be used for requesting certain things. 
    i.e. !caste to get the client's caste, !flightData to get all flight data, etc. 
    A list of all valid requests can be found in requests.txt
    """
    sk.sendall(f"!{item}".encode('utf-8'))

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
    complete = False
    # Create a TCP/IP socket
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (serverIP, pap) # Server's local IP, port
    print(f"{sys.stderr}\nConnecting to {serverIP} via port {pap} for port assignment.")
    cPort = sku.getPort(sk, server_address)
    server_address = (serverIP, cPort) # Server's local IP, assigned port
    sk.bind(server_address) # Connect to new server address
    sk.listen(1)
    sku.send("connected") # Tell server connection works, server will disconnect

    # Can't run the following until client and server are reconnected, otherwise client will close connection
    # while True:
    #     try:
    #         sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #         sk.connect(server_address)
    #         message = bInput("Message: ")
    #         if message == "quit":
    #             complete = True
    #             break
    #         sk.sendall(message)
    #     except:
    #         break
    # sk.close()
    # if complete:
    #     return ""
    # else:
    #     return "ensure server IP and port are correct"




if __name__ == "__main__":
    stp = setup()
    if stp == "":
        # do other stuff
        print("Done.")
    else:
        print(f"FATAL: Unable to complete setup - {stp}")

# SS71 plane, angel of death