import socket

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get the IP address and port of the server
ip_address = socket.gethostbyname("google.com")
port = 80

# connect to the server
client_socket.connect((ip_address, port))

# send a GET request to the server
client_socket.sendall(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# receive data from the server
response = client_socket.recv(4096)

# print the received data
print("Response from the server: ", response)

# close the socket
client_socket.close()
