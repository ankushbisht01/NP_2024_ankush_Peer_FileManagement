import socket

def send_file(conn, filename):
    try:
        with open(filename, 'rb') as file:
            file_data = file.read()
            conn.sendall(file_data)
        print(f"Sent '{filename}' to client successfully.")
    except FileNotFoundError:
        conn.sendall(b"File not found")

def main():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connected to client: {addr}")

        filename = conn.recv(1024).decode()
        if filename:
            print(f"Received request for file: {filename}")
            send_file(conn, filename)

        conn.close()

if __name__ == '__main__':
    main()
