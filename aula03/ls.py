from subprocess import Popen
from subprocess import PIPE
from sys import argv

if len(argv) != 3:
    print(f"Usage: python3 {argv[0]} [dir] [exclude_term]")
    exit()

proc = Popen(f"ls -la {argv[1]}", stdout=PIPE, shell=True)

return_code = proc.wait()

for line in iter(proc.stdout.readline, b""):
    line = line.decode("utf-8")
    if argv[2] in line:
        print(line, end="")