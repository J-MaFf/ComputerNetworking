# server.py
import math
import socket

def main():
    initiateConnection()

def initiateConnection():
    """
    Function to initiate a connection with a client.

    This function binds a socket to a specific IP address and port,
    listens for incoming connections, and establishes a connection
    with a client. It then sends a 'hello' message to the client and
    enters a loop to receive and send data until the connection is closed.
    """
    HOST = "127.0.0.1" # The server's hostname or IP address
    PORT = 7777 # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #                     (^ IPV4     ,      ^ TCP)
        s.bind((HOST, PORT)) # 2 sets of () because bind requires a tuple
        s.listen() 
        conn, addr = s.accept() # Blocks until a connection is made
        ''' con = new socket object usable to send and receive data
            on the connection, addr = address bound to the socket on
            the other end of the connection
        '''
        with conn:
            print(f"Connected to {addr}")
            num = math.random(1, 100) # Generate a random integer from 1 to 99 (inclusive)

            conn.sendall(b'hello') # Send a 'hello' message to the client (b = bytes)
            while True:
                data = conn.recv(1024) 
                if not data:
                    break
                else:
                    game(data, num, conn)
                conn.sendall(data)
    
def game(message, num, conn):
    """
    This function plays a number guessing game.

    Parameters:
    - message (bytes): The message received from the client.
    - num (int): The target number to guess.
    - conn (socket object): The connection object representing the client connection.
    """
    message = message.decode('ascii').lower() # Decode the message using ASCII encoding
    # Parse message
    if (message == "quit"):
        conn.close()
    else:
        guess = int(message) # needs error handling
    # Compare guess to num
    if (guess == num):
        conn.sendall("correct")
        conn.close()
    elif (guess > num):
        conn.sendall("too-high")
    else:
        conn.sendall("too-low")

if __name__ == "__main__": # Only run the code if this file is run directly
    main()