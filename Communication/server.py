import socket
import sys

#0-2^16-1 port range
def create_socket():
    
    try:        
        global host
        global port
        global skt
        
        host = ""
        port = 8080
        
        skt=socket.socket()
    
    except socket.error as msg:
        
        print("Socket creation error: ",str(msg))
        
def socket_bind_and_listen():
    
    try:
        global host
        global port
        global skt 
        
        skt.bind((host,port))
        skt.listen()
        
    except socket.error as msg:
        print("Socket binding error: ", str(msg))
        socket_bind_and_listen()
         
def socket_accept_connection():
    connection,address = skt.accept()
    
    print("Client IP   :  ",address[0])
    print("Client Port:  ",address[1])
    
    sending_commands()
    
    connection.close()
     
    
def main():
    create_socket()
    
main()
