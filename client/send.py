import socket 
import os 
from tqdm import tqdm
import json

def send_file(chunks: list, host: str, port: int):
    chunk_size = os.path.getsize(chunks[0])
    length = len(chunks)
    #progress_bar = tqdm(total=chunk_size*length, unit="B", unit_scale=True)
    for chunk_path in chunks:
        # Create a socket object
        s = socket.socket()
        # print(f"Connecting to {host}:{port}")
        try:

            # Set a timeout for the connection

            s.settimeout(20)  # 10 seconds timeout
            s.connect((host, port))
            # print(f"Connected to {host}:{port}")

            #send command to the server
            s.send(b"send")

            ack = s.recv(1024).decode()


            # Send the file name 
            s.sendall(chunk_path.encode())

            ack = s.recv(1024).decode()

            print(f"Server response: {ack}")

            
            # Send the file
            with open(chunk_path, "rb") as file:
                
                while True:
                    # Read 1024 bytes from the file
                    bytes_read = file.read(1024)
                    if not bytes_read:
                        # File transmission is done
                        break
                    # We use sendall to assure transmission in busy networks
                    s.sendall(bytes_read)
                    
            #update the progressbar with the size of the file
            #progress_bar.update(chunk_size)
        except socket.timeout:
            print("Connection timed out.")
        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            # Close the socket
            s.close()
            # print("Connection closed.")

    # progress_bar.close()    


def recieve_file(host: str, port: int , chunks:list):
    for filename in chunks:
            
            host = '127.0.0.1'
            port = port

            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((host, port))

            #send command to the server
            client_socket.send(b"receive")

            ack = client_socket.recv(1024).decode()

    

            client_socket.send(filename.encode())
            response = client_socket.recv(1024).decode()

            print(f"Server response: {response}")

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


