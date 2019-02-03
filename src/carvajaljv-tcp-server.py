# File Name: carvajaljv-tcp-server.py
# Author:    John Carvajal
# Class:     Computer Networking 425
# Teacher:   Dr. Glendowne
# Date:      1/30/2018
# Description: Create a simple tcp client and tcp server using sockets and Python 3
# This program should send a random integer (range 1 to 10,000) to the server. The server 
# should display the received number and send an acknowledgement back. The acknowledgement 
# in this case is just a string. It can be anything you want.

print('Program has started')
print('Written by John Carvajal')
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
#print >>sys.stderr, 'starting up on %s port %s' % server_address
print ('server program has started')
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # wait for a connection
    print ('Waiting for connection...')
    connection, client_address = sock.accept()

    try:
        print ('*RING RING RING*')
        print ('connection from', client_address)
        print ('Hello? This is Mr. Server here!')

        # recieve data and send back
        while True:
            data = connection.recv(128)
            print ('received "%s"' % data)
            if data:
                print ('Awesome, thanks Mr. Client man! Thats exactly what I needed!')
                message = ('Awesome, thanks Mr. Client man! Thats exactly what I needed!')
                connection.sendall(message)
            else:
                print ('no more data from', client_address)
                break
            
    finally:
        # close the connection
        connection.close()