import socket

def start_client(host="127.0.0.1", port=5000):
    # Create TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server
    client_socket.connect((host, port))
    print(f"Connected to server {host}:{port}")

    while True:
        msg = input("Enter message (or 'exit' to quit): ")

        if msg.lower() == "exit":
            break

        # Send message
        client_socket.sendall(msg.encode())

        # Receive echo
        data = client_socket.recv(1024)
        print("Server echoed:", data.decode())

    client_socket.close()

if __name__ == "__main__":
    start_client()
