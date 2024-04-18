from compress import compress, decompress
from encrypt import encrypt, decrypt
from split import split_file_into_chunks, combine_chunks
from send import send_file , recieve_file
from store import store_data
from tqdm import tqdm
import os
import json
import glob


def sort_key(file_path):
    # Extract the numeric part after "temp\\" and convert to integer
    return int(file_path.split("\\")[1].split("-")[0])



def main():
    filename = input("Enter the filename: ")
    filename = os.path.join("Data", filename)
    
    print("[+] Reading file  " , filename )
    with open(filename, "rb") as file:
        data = file.read()
    print("[+] File read successfully")
    print("[+] Compressing data")
    compressed_data = compress(data)
    print("[+] Data compressed successfully")
    print("[+] Encrypting data")
    # encrypted_compressed_data = encrypt(compressed_data)
    print("[+] Data encrypted successfully")
    with open("compressed.xz", "wb") as file:
        file.write(compressed_data)
    print("[+] Data written to file")
    print("[+] Splitting file into chunks")
    chunks = split_file_into_chunks("compressed.xz")
    print("[+] File splitted into chunks")
    
    # remove the compressed file if it exists
    if os.path.exists("compressed.xz"):
        os.remove("compressed.xz")



    store_data(chunks, 2)

    #read the json file
    with open("data.json", "r") as file:
        data = file.read()

    data = json.loads(data)

    first_server = data["Host0"]["chunks"]
    second_server = data["Host1"]["chunks"]

    

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
    whole_chunks.sort(key=sort_key)
    combine_chunks(whole_chunks , "output.xz")


    output_file = input("Enter the output filename: ")
    output_file = os.path.join("Output", output_file)

    with open("output.xz" , "rb") as file:
        data = file.read()
    # decompressed_data = decrypt(data)
    decompressed_data = decompress(data)


    with open(output_file , "wb") as file:
        file.write(decompressed_data)

    if os.path.exists("output.xz"):
        os.remove("output.xz")


    
    
if __name__ == "__main__":
    choice = """
    1. Send file
    2. Receive file
            """
    
    input_choice = int(input(choice))
    if input_choice == 1:
        main()
    elif input_choice == 2:
        get_chunks()
    else:
        print("Invalid choice")

    

