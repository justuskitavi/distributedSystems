import socket

def start_server(host="127.0.0.1", port=5000):
    # Create TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind to address
    server_socket.bind((host, port))
    print(f"Server started on {host}:{port}")

    # Listen for incoming connections
    server_socket.listen(1)
    print("Server is listening for connections...")

    # Accept a connection
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    # Handle client messages
    while True:
        data = conn.recv(1024)
        if not data:
            break

        print("Client:", data.decode())
        
        # Echo the message back
        conn.sendall(data)

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
