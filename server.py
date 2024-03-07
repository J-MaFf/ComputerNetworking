# server.py
import math
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
    
def game():
    num = math.random(1, 100) # Generate a random integer from 1 to 99 (inclusive)


''' Create a TCP stream socket bound to 127.0.0.1 and port 7777 to listen for incoming clients

    Loop forever to listen for connections

    Accept an incoming connection, creating a socket for that client

    // Generate a random integer from 1 to 99 (inclusive)

    // Send a 'hello' message to the client

    // Loop forever to receive new messages from this client

    // 		Receive an incoming message and decode it using ASCII encoding

    // 		If the message is a 'quit' message, disconnect from this client and start listening again

    // 		If the message is a 'guess' message, parse the client's guess, then...

    // 			...If their guess matches the answer, send a 'correct' message to them and disconnect from the client
    
    // 			...If their guess is greater than the answer, send a 'too-high' message and continue listening

    // 			...If their guess is less than the answer, send a 'too-low' message and continue listening
	'''

if __name__ == "__main__": # Only run the code if this file is run directly
    main()