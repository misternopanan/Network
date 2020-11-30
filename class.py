import socket
import time
 
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
 
# Bind the socket to the port
server_address = ('localhost', 8002) 
print('starting up on %s port %s' % server_address)
sock.bind(server_address)
sock.listen(1) 
 
while True:
    connection, client_address = sock.accept() 
    server_wait = True
    try:
        while server_wait:
            try:
                data = connection.recv(300) 
                if not data: server_wait = False 
                print('Server Recv and Send back : ',data.decode("utf-8")) 
                connection.sendall(data) 
            except :
                server_wait = False
 
    finally:
        # Clean up the connection
        connection.close() 