import socket

# get the hostname of Amazon's server
hostname = "amazon.com"

# get the IP address of the host
ip_address = socket.gethostbyname(hostname)

# print the IP address
print("IP address of", hostname, "is:", ip_address)
