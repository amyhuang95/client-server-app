import socket

# Create a socket object
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Connect to the server
HOST = ''
PORT = 6789
clientSocket.connect((HOST, PORT))
print("Connected to the server")

message = ("GET /HelloWorld.html HTTP/1.1\n"
"Host: 10.152.196.97:6789\n"
"Connection: keep-alive\n"
"DNT: 1\n"
"Upgrade-Insecure-Requests: 1\n"
"User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36\n"
"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7\n"
"Accept-Encoding: gzip, deflate\n"
"Accept-Language: en-US,en;q=0.9,zh;q=0.8,zh-TW;q=0.7,zh-CN;q=0.6,ko;q=0.5\n")
clientSocket.send(message.encode()) # Send the message to the server

response = clientSocket.recv(2048).decode()
print(response)
    
# Close the connection
clientSocket.close()
