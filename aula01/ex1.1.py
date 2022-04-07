import hashlib
import sys

files = sys.argv
files.pop(0)

def calcHash(file):
    h = hashlib.sha1()
    with open(file, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def main():
    for file in files:
        print(calcHash(file), file, sep="  ")

main()