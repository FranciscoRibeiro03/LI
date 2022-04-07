import os
import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import ARC4

def main(fileToDecrypt, privateKeyFileName, password):
    privateKeyFile = open(privateKeyFileName, "r")
    privateKey = RSA.importKey( privateKeyFile.read(), password )

    with open(fileToDecrypt, "rb") as file:
        content = file.read()

    key = content[-128:]

    newContent = content[:-128]
    
    decryptedKey = decryptKeyWithRSA(key, privateKey)
    decryptedContent = decryptWithRC4(newContent, decryptedKey)

    os.write(1, decryptedContent)

def decryptWithRC4(content, key):
    cipher = ARC4.new(key)
    return cipher.decrypt(content)

def decryptKeyWithRSA(key, privateKey):
    cipher = PKCS1_OAEP.new( privateKey )
    return cipher.decrypt( key )


if len(sys.argv) < 3:
    print("Usage: python3 {} <file> <privateKeyFile> <passsword>".format(sys.argv[0]))
    sys.exit(1)

fileToDecrypt = sys.argv[1]
privateKeyFileName = sys.argv[2]
password = sys.argv[3]
main(fileToDecrypt, privateKeyFileName, password)