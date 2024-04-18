from encrypt import encrypt, decrypt
import lzma

def compress(data:bytes):
    """
    data : bytes
    Data to compress

    Returns compressed data

    Example:

    data = b"Hello, World!"
    compressed_data = compress(data)
    """
    return lzma.compress(data)



def decompress(data:bytes):
    """
    data : bytes
    Data to decompress

    Returns decompressed data

    Example:

    data = b"Hello, World!"
    compressed_data = compress(data)
    decompressed_data = decompress(compressed_data)

    """
    return lzma.decompress(data)



def main():
    # file_name = "input.wav"
    # with open(file_name, "rb") as file:
    #     data = file.read()
    # # encrypted_data = encrypt(data)
    # compressed_data = compress(data)
    # encrypted_compressed_data = encrypt(compressed_data)
    # with open("compressed.xz", "wb") as file:
    #     file.write(encrypted_compressed_data)

    with open("compressed.xz", "rb") as file:
        encrypted_compressed_data = file.read()
    decrypted_compressed_data = decrypt(encrypted_compressed_data)
    decompressed_data = decompress(decrypted_compressed_data)
    with open("decompressed.wav", "wb") as file:
        file.write(decompressed_data)

        
if __name__ == "__main__":
    main()