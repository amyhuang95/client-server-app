import socket
# !lsof -i :5555 —-> Lists any processes that are listening
# !kill -9 <PID> --> Ends connection (Sends the SIGKILL signal to the process specified by <PID>)


def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a local address and port
    # binding the socket to localhost and port 5555
    server_socket.bind(('127.0.0.1', 5555))
