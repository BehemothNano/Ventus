"""
A small library of shared functions for drone communication via python's socket library.

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

validRequests = []

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

def send(sk, thing):
    sk.sendall(thing.encode('utf-8'))
    return True

def testLatency_Client(sk, clientID):
    """ Tests the latency from the client to the server. """
    t1_client = time.time()
    request(sk, f"!latency | {clientID}, {t1_client}")
    t1_server = receive(sk)
    t2 = time.time()
    serverToClient = t2 - t1_server
    total = t2 - t1_client
    return serverToClient, total

def testLatency_Server(sk, clientID, t1_client, address):
    """ Tests the latency from the client to the server. Called on server when receive returns !latency | args."""
    t1_server = time.time()
    sk.bind(address) # not unnecessary as the two latency functions may be initiated at different times | actually it might be, will have to see
    send(sk, f"T:{t1_server}")
    request(sk, f"!endLatency | {clientID}")
    return t1_server - t1_client # Client to Server


def request(sk, request):
    """ 
    To be used for requesting certain things. 
    i.e. !caste to get the client's caste, !flightData to get all flight data, etc. 
    A list of all valid requests can be found in requests.txt
    """
    sk.sendall(f"!{request}".encode('utf-8'))

def getValidRequests(filepath):
    """
    Generates a dictionary of valid requests (actually just updates the global validRequests dict)
    """
    with open(filepath, "r") as infile:
        for line in infile:
            if line[0] == "!":
                line = line.strip("! ")
                if "|" in line:
                    line = line.split("|")

def getRequest(data):
    """
    Name is a bit misleading, but essentially a massive match: case function 
    that determines what to do with different requests from requests.txt.
    """
    if validRequests == {}:
        # Update if the dict of valid requests doesn't exist yet, otherwise do nothing.
        getValidRequests()
    if request not in validRequests:
        return None
    match data:
        case "updateRequests":
            return x

def receive(sk):
    """
    Gets whatever was last sent, note that the while loop doesn't 
    make it keep getting things, but makes it so that it doesn't 
    have to be run as the thing is sent. If a lot of things were sent, 
    it would probably keep getting them until there aren't any more.
    * Hasn't been tested
    """
    connection, ca = sk.accept()
    while True:
        data = connection.recv(1024).decode('utf-8')
        if not data:
            break
        connection.send(data) # Why is this here?
    connection.close()
    return data

def receiveOnce(sk):
    """
    Gets whatever was last sent, though strictly limited to one item.
    """
    connection, ca = sk.accept()
    while True:
        data = connection.recv(1024)
        if not data:
            break
    connection.close()
    return data.decode('utf-8')

def getPort(sk, address)
    """
    Gets port assignment for a client
    """
    sk.bind(address)
    sk.listen(1)
    receive(sk)
    return port