import socket
import threading

# Function to receive messages from the server
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            print(message)
        except:
            print("An error occurred. Unable to receive messages.")
            break

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(('127.0.0.1', 5555))

# Start a thread to receive messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Send messages to the server
while True:
    message = input()
    if message.lower() == 'exit':
        break
    client_socket.send(message.encode("utf-8"))

# Close the client socket
client_socket.close()
