import socket

# Define server address and port
SERVER_HOST = '127.0.0.1'  # localhost
TCP_PORT = 12345

def tcp_server():
    # Create a TCP socket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind((SERVER_HOST, TCP_PORT))
    tcp_socket.listen(1)
    print(f"TCP Server is listening on {SERVER_HOST}:{TCP_PORT}")

    # Accept an incoming connection
    client_socket, client_address = tcp_socket.accept()
    print(f"TCP Connection established with {client_address}")

    # Receive message from client
    message = client_socket.recv(1024).decode('utf-8')
    print(f"Received from TCP client: {message}")

    # Send a response back to the client
    client_socket.send("Hello from TCP Server".encode('utf-8'))

    # Close the connection
    client_socket.close()
    tcp_socket.close()

if __name__ == "__main__":
    tcp_server()
