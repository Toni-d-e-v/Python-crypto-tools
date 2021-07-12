# Inspired from https://medium.com/@ismailakkila/black-hat-python-encrypt-and-decrypt-with-rsa-cryptography-bd6df84d65bc
# Updated to use python3 bytes and pathlib
#encrypt.py it will encrpyt a file

import zlib
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from pathlib import Path




#Our Encryption Function
def encrypt_blob(blob, public_key):
    #Import the Public Key and use for encryption using PKCS1_OAEP
    rsa_key = RSA.importKey(public_key)
    rsa_key = PKCS1_OAEP.new(rsa_key)

    #compress the data first
    blob = zlib.compress(blob)
    #In determining the chunk size, determine the private key length used in bytes
    #and subtract 42 bytes (when using PKCS1_OAEP). The data will be in encrypted
    #in chunks
    chunk_size = 470
    offset = 0
    end_loop = False
    encrypted = bytearray()
    while not end_loop:
        #The chunk
        chunk = blob[offset:offset + chunk_size]
        #If the data chunk is less then the chunk size, then we need to add
        #padding with " ". This indicates the we reached the end of the file
        #so we end loop here
        if len(chunk) % chunk_size != 0:
            end_loop = True
            #chunk += b" " * (chunk_size - len(chunk))
            chunk += bytes(chunk_size - len(chunk))
        #Append the encrypted chunk to the overall encrypted file
        encrypted += rsa_key.encrypt(chunk)
        #Increase the offset by chunk size
        offset += chunk_size
    #Base 64 encode the encrypted file
    return base64.b64encode(encrypted)
#Our Decryption Function




new_key = RSA.generate(4096, e=65537)

#The private key in PEM format


#The public key in PEM Format
public_key = new_key.publickey().exportKey("PEM")

print('FILE WILL NOT BE REVIVED EVER! DO THIS AT YOUR OWN RISK!!!')

print('File that you want to destroy:')
unencrypted_file = Path(input())
i = 0
while i < 5:
    encrypted_msg = encrypt_blob(unencrypted_file.read_bytes(), public_key)
    fd = open(unencrypted_file, "wb")
    fd.write(encrypted_msg)
    print(i)
    i = i +1
    fd.close()

