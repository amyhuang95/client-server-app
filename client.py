import socket

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect(('127.0.0.1', 5555)) # Connect to localhost and port 5555
    print("Connected to the server")

    # Send and receive messages
    while True:
        message = input("Enter a message to send to the server (or type 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        client_socket.send(message.encode()) # Send the message to the server
        response = client_socket.recv(1024).decode() # Receive the response from the server
        print(f"From the server: {response}")

    # Close the connection
    client_socket.close()

# Start the client
start_client()