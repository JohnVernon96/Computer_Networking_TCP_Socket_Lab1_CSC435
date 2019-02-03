# File Name: carvajaljv-tcp-client.py
# Author:    John Carvajal
# Class:     Computer Networking 425
# Teacher:   Dr. Glendowne
# Date:      1/30/2018
# Description: Create a simple tcp client and tcp server using sockets and Python 3
# This program should send a random integer (range 1 to 10,000) to the server. The server 
# should display the received number and send an acknowledgement back. The acknowledgement 
# in this case is just a string. It can be anything you want.

import socket
import random
number = random.randint(1, 10000)

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the socket
server_address = ('localhost', 10000)
print ( 'connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    # send the data
    message = 'Ayyee whats up man, its the client.py here. just wanted to give you this number: '+str(number)
    print ('sending "%s"' % message)
    sock.sendall(message)

    # look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(128)
        amount_received += len(data)
        print ('received "%s"' % data)

finally:
    print ('closing socket')
    #close the connection
    sock.close()