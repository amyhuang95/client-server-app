import socket, sys

# Create a socket object
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Connect to the server
HOST = 'localhost'
PORT = 6789
clientSocket.connect((HOST, PORT))
print("Connected to the server")

# Test a page
filename = sys.argv[1]
print(f'File path: {filename}')
http_request = (f"GET /{filename} HTTP/1.1\n")
clientSocket.send(http_request.encode())
http_response = clientSocket.recv(2048).decode().split('\n')[0]
print(http_response)

    
# Close the connection
clientSocket.close()
