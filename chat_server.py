import socket
import threading
def handle_client(client_socket, client_address):
    print(f"Connection from {client_address}")
    while True:
        message = client_socket.recv(1024).decode("utf-8")
        if not message:
            break
        print(f"Received from {client_address}: {message}")
        broadcast(message, client_socket)
    print(f"Disconnected from {client_address}")
    client_socket.close()

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode("utf-8"))
            except:

                clients.remove(client)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('127.0.0.1', 5555))

server.listen(5)
print("Server is listening...")
clients = []

while True:
    client_socket, client_address = server.accept()
    clients.append(client_socket)
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
