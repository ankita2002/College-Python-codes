#socket_server
import socket

def server_program():
    #get host name
    host = socket.gethostname()
    #initiate port no above 1024
    port = 5000
    #get instance
    server_socket = socket.socket()
    #look closely. the bind() function takes tuple as argument
    server_socket.bind((host, port))
    #bind host ADDRESS and port together
    #configure how many client the server can listen simultaneosuly 
    server_socket.listen(2)
    #accept new connection
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:
        #receive data stream, wont accept data packet greater than 1024 bytes 
        data = conn.recv(1024).decode()
        if not data:
            #if data is not received break
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        #send data to client 
        conn.send(data.encode())
        conn.close()
        # close connection

if __name__ == '__main__':
    server_program()