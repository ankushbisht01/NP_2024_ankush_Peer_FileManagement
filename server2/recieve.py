import socket 
import sys
import os 
import glob
import tqdm

def recieve_file(chuck_path: str, host: str, port: int):
    # Create a socket object
    s = socket.socket()
    print(f"Connecting to {host}:{port}")
    #bind the socket to the address
    s.bind((host, port))

    #listen for connections
    s.listen(5)

    while True:
        #accept connections
        client_socket, client_address = s.accept()
        print(f"Connected to {host}:{port}")
        

        #get the file name
        filename = client_socket.recv(1024).decode()
        client_socket.send("Filename recieved".encode())

        # chuck_path = os.path.join(chuck_path, filename)
        chuck_path = filename


        #send ack 
        client_socket.send("ACK".encode())

        # Send the file
        with open(chuck_path, "wb") as file:
            print(f"Recieving {chuck_path}...")
            while True:
                # Read 1024 bytes from the file
                bytes_read = s.recv(1024)
                if not bytes_read:
                    # File transmission is done
                    break
                # We use sendall to assure transmission in busy networks
                file.write(bytes_read)
        print(f"Recieved {chuck_path}")

        
        #clear the filename buffer
        filename = ""

        # Close the socket
        client_socket.close()

    s.close()



def main():
    PORT = 5051
    HOST = "127.0.0.1"
    recieve_file("temp", HOST, PORT)

if __name__ == "__main__":
    main()
    


