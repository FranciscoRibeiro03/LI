"""
Faça um programa em Python que gere um par de chaves e que o guarde num ficheiro.
O programa deverá ter como parâmetros o nome do ficheiro para o par de chaves, a
chave de cifra e o número de bits da chave.
"""
import sys
from Crypto.PublicKey import RSA

if (len(sys.argv) != 4):
    print("Usage: python3 {} nome chave nBits".format(sys.argv[0]))
    exit(1)

nome = sys.argv[1]
chave = sys.argv[2]
nBits = int(sys.argv[3])

keypair = RSA.generate(nBits)
fout = open(f"{nome}.pem", "wb")

with open(f"{nome}.pem", "wb") as fout:
    kp = keypair.exportKey("PEM", chave)
    fout.write(kp)

with open(f"{nome}.pub", "wb") as fout:
    kp = keypair.publickey().exportKey("PEM")
    fout.write(kp)