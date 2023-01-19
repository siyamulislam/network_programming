import socket

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# define the server address and port
server_address = ("127.0.0.1", 1234)

# send data to the server
message = "Hello, Server!"
client_socket.sendto(message.encode(), server_address)

# receive data from the server
data, server = client_socket.recvfrom(1024)

# print the received data
print("Received from server: ", data.decode())

# close the socket
client_socket.close()
