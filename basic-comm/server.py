import socket

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific address and port
server_socket.bind(("127.0.0.1", 1234))

# listen for incoming connections
server_socket.listen(5)

while True:
    # establish a connection
    client_socket, addr = server_socket.accept()
    print("Got a connection from %s" % str(addr))

    # receive data from the client
    data = client_socket.recv(1024)
    print("Received: %s" % data)

    # send a message to the client
    message = "Thank you for connecting"
    client_socket.send(message.encode())

    # close the connection
    client_socket.close()
