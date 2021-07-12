# Inspired from https://medium.com/@ismailakkila/black-hat-python-encrypt-and-decrypt-with-rsa-cryptography-bd6df84d65bc
# Updated to use python3 bytes and pathlib
#getkeys.py it will generate set of rsa keys

import zlib
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from pathlib import Path


def generate_new_key_pair():
    #Generate a public/ private key pair using 4096 bits key length (512 bytes)
    new_key = RSA.generate(4096, e=65537)

    #The private key in PEM format
    private_key = new_key.exportKey("PEM")

    #The public key in PEM Format
    public_key = new_key.publickey().exportKey("PEM")

    private_key_path = Path('private.pem')
    private_key_path.touch(mode=0o600)
    private_key_path.write_bytes(private_key)

    public_key_path = Path('public.pem')
    public_key_path.touch(mode=0o664)
    public_key_path.write_bytes(public_key)





generate_new_key_pair() # run if you don't already have a key pair
print('Keys creted:private.pem,public.pem')