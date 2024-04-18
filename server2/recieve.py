import socket
import os 
from tqdm import tqdm

def recieve_file(host: str, port: int):
    # Create a socket object
    s = socket.socket()
    s.bind((host, port))
    s.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        print("Waiting for connection...")
        conn, addr = s.accept()
        print(f"Connected by {addr}")

        try:
            # Receive the file name
            file_name = conn.recv(1024).decode()

            # Send a response
            conn.sendall(b"File name received")

            if file_name:
                #get file from the client
                file_data = b""
                print(f"Receiving '{file_name}'...")
                while True:
                    bytes_read = conn.recv(1024)
                    if not bytes_read:
                        break
                    file_data += bytes_read
                with open(file_name, "wb") as file:
                    file.write(file_data)
                print(f"Received '{file_name}' successfully.")
                
            else:
                print("No file name received")

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            # Close the connection
            conn.close()
            print("Connection closed.")


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
    port = 5051

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

def reciever_main():
    host = '127.0.0.1'
    port = 5051
    recieve_file(host, port)


if __name__ == "__main__":
    main()
    


