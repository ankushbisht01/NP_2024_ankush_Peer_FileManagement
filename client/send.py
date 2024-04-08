import socket 

def send_file(chunks: list, host: str, port: int):
    # Create a socket object
    s = socket.socket()
    print(f"Connecting to {host}:{port}")
    try:
        # Set a timeout for the connection
        s.settimeout(10)  # 10 seconds timeout
        s.connect((host, port))
        print(f"Connected to {host}:{port}")

        # Send each chunk
        for chunk_path in chunks:
            # Send the file name 
            s.sendall(chunk_path.encode())

            # Receive the response
            response = s.recv(1024).decode()
            print(f"Server response: {response}")

            # Send the file
            with open(chunk_path, "rb") as file:
                print(f"Sending {chunk_path}...")
                while True:
                    # Read 1024 bytes from the file
                    bytes_read = file.read(1024)
                    if not bytes_read:
                        # File transmission is done
                        break
                    # We use sendall to assure transmission in busy networks
                    s.sendall(bytes_read)
            print(f"Sent {chunk_path}")

    except socket.timeout:
        print("Connection timed out.")
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the socket
        s.close()
        print("Connection closed.")