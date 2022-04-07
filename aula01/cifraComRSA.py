import os
import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import ARC4

def main(fileToEncrypt, publicKeyFileName):
    publicKeyFile = open(publicKeyFileName, "r")
    publicKey = RSA.importKey( publicKeyFile.read() )
    cipher = PKCS1_OAEP.new( publicKey )

    with open(fileToEncrypt, "rb") as file:
        content = file.read()

    key = os.urandom(64)
    
    encryptedContent = encryptWithRC4(content, key)
    encryptedKey = encryptKeyWithRSA(key, publicKey)

    x = encryptedContent + encryptedKey

    os.write(1, x)

def encryptWithRC4(content, key):
    cipher = ARC4.new(key)
    return cipher.encrypt(content)

def encryptKeyWithRSA(key, publicKey):
    cipher = PKCS1_OAEP.new( publicKey )
    return cipher.encrypt( key )


if len(sys.argv) < 3:
    print("Usage: python3 {} <file> <publicKeyFile>".format(sys.argv[0]))
    sys.exit(1)

fileToEncrypt = sys.argv[1]
publicKeyFileName = sys.argv[2]
main(fileToEncrypt, publicKeyFileName)