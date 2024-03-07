# server.py
import random
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
            num = random.randint(1,99) # Generate a random integer from 1 to 99 (inclusive)

            hello = 'hello\r\n'.encode('ascii') # Create a 'hello' message

            conn.sendall(hello) # Send a 'hello' message to the client (b = bytes)
            while True:
                data = conn.recv(1024) 
                if not data:
                    break
                else:
                    game(data, num, conn)
                #conn.sendall(data)
    
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
    if (message == "quit\r\n"):
        print("Connection closed by client.")
        return
    else:
        parts = message.split('\t')  # Split the string on the tab character
        if len(parts) < 2:
            print("Invalid message format received from client.")
            return
        guess_str = parts[1].strip()  # Get the second part and remove any leading/trailing whitespace
        guess = int(guess_str)  # Convert the string to an integer
    # Compare guess to num
    if (guess == num):
        conn.sendall("correct\r\n".encode('ascii'))
        print("Correct guess, connection closing...")
        return
    elif (guess > num):
        conn.sendall("too-high\r\n".encode('ascii'))
    else:
        conn.sendall("too-low\r\n".encode('ascii'))

if __name__ == "__main__": # Only run the code if this file is run directly
    main()