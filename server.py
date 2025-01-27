import socket
# !lsof -i :5555 —-> Lists any processes that are listening
# !kill -9 <PID> --> Ends connection (Sends the SIGKILL signal to the process specified by <PID>)


def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a local address and port
    server_socket.bind(('127.0.0.1', 5555)) # binding the socket to localhost and port 5555

    # Start listening for connections
    server_socket.listen(1)
    print("Server is listening on port 5555... waiting for one client")

    # Accept a connection
    connection_socket, addr = server_socket.accept() # blocking call
    print(f"Connection established with client {addr}")

    # Receive data from the client
    while True:
        sentence = connection_socket.recv(1024).decode() # Receive a message (buffer size: 1024 bytes)
        if not sentence:
            print("Client disconnected")
            break
        print(f"From the client: {sentence}")
        capitalized_sentence = sentence.upper()
        print(f"To the client: {capitalized_sentence}")
        connection_socket.send(capitalized_sentence.encode()) # Send the capitalized message back to the client

    # Close the connection
    connection_socket.close()
    server_socket.close()

# Run the server in a thread
start_server()
