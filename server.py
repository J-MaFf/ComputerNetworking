# server.py
import socket

def main():
    initiateConnection()

def initiateConnection():
    HOST = "127.0.0.1" # The server's hostname or IP address
    PORT = 7777 # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #                     (^ IPV4     ,      ^ TCP)
        s.bind((HOST, PORT)) # 2 sets of () because bind requires a tupple
        s.listen() 
        conn, addr = s.accept() # Blocks until a connection is made
        ''' con = new socket object usable to send and receive data
            on the connection, addr = address bound to the socket on
            the other end of the connection
        '''
        with conn:
            print(f"Connected to {addr}")
            while True:
                data = conn.recv(1024) 
                if not data:
                    break
                conn.sendall(data)

if __name__ == "__main__": # Only run the code if this file is run directly
    main()