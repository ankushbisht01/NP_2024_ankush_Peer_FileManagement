from cryptography.fernet import Fernet
from decouple import config


def encrypt(data:bytes):
    key = config('Key')
    #convert key into a bytes object
    key = key.encode()
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(data)
    return cipher_text

def decrypt(data:bytes):
    key = config('Key')
    key = key.encode()
    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(data)
    return plain_text



