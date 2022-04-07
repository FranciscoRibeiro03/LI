import hashlib
import sys

files = sys.argv
files.pop(0)

for file in files:
    f = open(file, "rb")
    buffer = f.read(512)
    h = hashlib.sha1()
    while len(buffer) > 0:
        h.update(buffer)
        buffer = f.read(512)
    print(h.hexdigest(), file, sep="  ")

