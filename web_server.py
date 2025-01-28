# import socket module
from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
HOST = 'localhost'
PORT = 6789
serverSocket.bind((HOST, PORT))
serverSocket.listen(1)
print(f"Server is listening on port {PORT}... waiting for one client")

while True:
    # Establish the connection when contacted by a client (browser)
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print(f"Connection established with client {addr}")
    try:
        # Receive the HTTP request
        message = connectionSocket.recv(2048).decode()
        # Parse the request to determine file name to be processed
        filename = message.split()[1]
        # Get the requested file from server's file system
        f = open(filename[1:])
        outputdata = f.read()
        # Send one HTTP header line into socket
        header = "HTTP/1.1 200 OK\r\n\n"
        connectionSocket.send(header.encode())
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        header = "HTTP/1.1 404 Not Found\n"
        connectionSocket.send(header.encode())
        # Close client socket
        connectionSocket.close()

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
