import socket
import threading

# Choosing a nickname
nickname = input("Choose a nickname: ")

# Connecting to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect(('127.0.0.1', 55555))  # Trying to connect to the server
except ConnectionError:
    print("Failed to connect to server.")
    exit()  # Exit if connection fails

# Receiving or listening messages from the server
def recieve():
    while True:
        try:
            message = client.recv(1024).decode('ascii')  # Receive message from server
            if message == 'NICK':  # If server asks for nickname
                client.send(nickname.encode('ascii'))  # Send nickname to server
            else:
                print(message)  # Print other messages
        except Exception as e:  # Catch and handle exceptions
            print(f"Error occurred: {e}")
            client.close()
            break  # Exit the loop if there’s an error

# Function for sending messages (write)
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))  # Format message
        client.send(message.encode('ascii'))  # Send message to server

# Multi-threading for both receiving and writing
recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
