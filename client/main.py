from compress import compress, decompress
from encrypt import encrypt, decrypt
from split import split_file_into_chunks, combine_chunks
from send import send_file , recieve_file
from store import store_data
from tqdm import tqdm
import os
import json
import glob


def main():
    filename = "input.wav"
    
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
    
    #remove the compressed file if it exists
    if os.path.exists("compressed.xz"):
        os.remove("compressed.xz")



    store_data(chunks, 2)

    #read the json file
    with open("data.json", "r") as file:
        data = file.read()

    data = json.loads(data)

    first_server = data["Host0"]["chunks"]
    second_server = data["Host1"]["chunks"]

    print(first_server)

    send_file(first_server , "127.0.0.1" , 5050)
    send_file(second_server , "127.0.0.1" , 5051)

def get_chunks():
    with open("data.json", "r") as file:
        data = file.read()

    data = json.loads(data)

    first_server = data["Host0"]["chunks"]
    second_server = data["Host1"]["chunks"]

    recieve_file("127.0.0.1" , 5050 , first_server)
    recieve_file("127.0.0.1" , 5051 , second_server)

    whole_chunks = glob.glob("temp/*")
    combine_chunks(whole_chunks , "output.xz")

    with open("output.xz" , "rb") as file:
        data = file.read()
    decompressed_data = decrypt(data)
    decompressed_data = decompress(decompressed_data)

    with open("output.wav" , "wb") as file:
        file.write(decompressed_data)

    if os.path.exists("output.xz"):
        os.remove("output.xz")


    
    
if __name__ == "__main__":
    get_chunks()

    

