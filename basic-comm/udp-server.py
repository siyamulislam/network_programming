import socket

# create a socket object
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind the socket to a specific address and port
udp_socket.bind(("127.0.0.1", 12345))

# receive data from the socket
data, addr = udp_socket.recvfrom(1024)

# print the received data
print("Received data: ", data)

# close the socket
udp_socket.close()
