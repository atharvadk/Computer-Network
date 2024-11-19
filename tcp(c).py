import socket

# Define server address and port
SERVER_HOST = '127.0.0.1'  # localhost
TCP_PORT = 12345

def tcp_client():
    print("Using TCP...")
    
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    client_socket.connect((SERVER_HOST, TCP_PORT))
    
    # Send a message to the server
    client_socket.send("Hello from TCP Client".encode('utf-8'))
    
    # Receive a response from the server
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Received from server: {response}")
    
    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    tcp_client()
