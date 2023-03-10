import socket

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get the IP address and port of the server
ip_address = "127.0.0.1"
port = 1234

# connect to the server
client_socket.connect((ip_address, port))

# send a message to the server
message = "Hello, server"
client_socket.send(message.encode())

# receive data from the server
response = client_socket.recv(1024)
print("Received from server:", response.decode())

# close the socket
client_socket.close()
