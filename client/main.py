from compress import compress, decompress
from encrypt import encrypt, decrypt
from split import split_file_into_chunks, combine_chunks
from send import send_file
from tqdm import tqdm
import os

def main():
    filename = "input.wav"
    data = {
        "HostName":"127.0.0.1",
        "Host1" : {
            "PORT": 5050,
        },
        "Host2" : {
        
            "HostName":"127.0.0.1",
            "PORT": 5051,
        }
    }

    print("[+] Reading file  " , filename )
    with open(filename, "rb") as file:
        data = file.read()
    print("[+] File read successfully")
    print("[+] Compressing data")
    compressed_data = compress(data)
    print("[+] Data compressed successfully")
    print("[+] Encrypting data")
    encrypted_compressed_data = encrypt(compressed_data)
    print("[+] Data encrypted successfully")
    with open("compressed.xz", "wb") as file:
        file.write(encrypted_compressed_data)
    print("[+] Data written to file")
    print("[+] Splitting file into chunks")
    chunks = split_file_into_chunks("compressed.xz")
    print("[+] File splitted into chunks")
    
    print(chunks[:2])

    chunk1 = chunks[0]
    print(os.path.basename(chunk1))


    #assign the odd chunks to the second server and even chunk to the first server
    first_server = []
    second_server = []

    for i in range(len(chunks)):
        if i % 2 == 0:
            first_server.append(chunks[i])
        else:
            second_server.append(chunks[i])

    send_file(first_server , "127.0.0.1" , 5050)
    send_file(second_server , "127.0.0.1" , 5051)
if __name__ == "__main__":
    main()

    

