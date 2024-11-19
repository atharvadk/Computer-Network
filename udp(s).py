import socket

# Define server address and port
SERVER_HOST = '127.0.0.1'  # localhost
UDP_PORT = 12346

def udp_server():
    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((SERVER_HOST, UDP_PORT))
    print(f"UDP Server is listening on {SERVER_HOST}:{UDP_PORT}")

    # Receive message from client
    message, client_address = udp_socket.recvfrom(1024)
    print(f"Received from UDP client: {message.decode('utf-8')}")

    # Send a response back to the client
    udp_socket.sendto("Hello from UDP Server".encode('utf-8'), client_address)

    # Close the socket
    udp_socket.close()

if __name__ == "__main__":
    udp_server()
