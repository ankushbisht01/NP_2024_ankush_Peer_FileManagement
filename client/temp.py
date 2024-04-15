import socket

def receive_file_from_server(filenames: list):
    for filename in filenames:
        
        host = '127.0.0.1'
        port = 12345

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        client_socket.send(filename.encode())

        file_data = b""
        while True:
            chunk = client_socket.recv(1024)
            if not chunk:
                break
            file_data += chunk
        
        if file_data.startswith(b"File not found"):
            print(f"File '{filename}' not found on server.")
        else:
            
            #write file_data into the file
            with open(filename, "wb") as file:
                file.write(file_data)
            print(f"Received '{filename}' from server successfully.")
        client_socket.close()

def main():
    filename = ["temp\compressed.xz-1.chunk" , "temp\compressed.xz-3.chunk"]
    receive_file_from_server(filename)

if __name__ == '__main__':
    main()
