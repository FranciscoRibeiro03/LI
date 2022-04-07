import pytest
from subprocess import Popen
from subprocess import PIPE

def testar(args, outputEsperado):
    proc = Popen(f"python3 fibonacci.py {args}")
    return_code = proc.wait()
    output = proc.stdout.read().decode("utf-8")
    return return_code, output, output == outputEsperado


def test_invalid_args():
    print("Testa comportamento com argumentos inválidos")
    teste1 = testar("", "Usage: python3 fibonacci.py n")
    assert teste1[0] == 1
    assert teste1[2]
