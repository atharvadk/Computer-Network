import socket

# Define server address and port
SERVER_HOST = '127.0.0.1'  # localhost
UDP_PORT = 12346

def udp_client():
    print("Using UDP...")
    
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Send a message to the server
    client_socket.sendto("Hello from UDP Client".encode('utf-8'), (SERVER_HOST, UDP_PORT))
    
    # Receive a response from the server
    response, _ = client_socket.recvfrom(1024)
    print(f"Received from server: {response.decode('utf-8')}")
    
    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    udp_client()
