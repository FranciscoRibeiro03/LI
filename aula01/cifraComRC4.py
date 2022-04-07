import os
import sys
import hashlib
from Crypto.Cipher import ARC4

if len(sys.argv) < 2:
    print("Usage: {} <file> <key>".format(sys.argv[0]))
    sys.exit(1)

fileName = sys.argv[1]
key = sys.argv[2]

lenKey = len(key)

if lenKey < 5:
    key = hashlib.sha256(key).hexdigest()
elif lenKey > 256:
    key = key[:256]

cipher = ARC4.new(key)
cryptogram = cipher.encrypt(open(fileName, "rb").read())

os.write(1, cryptogram)