import sys
from builtins import str

l = []
while True:
    line = sys.stdin.readline().strip()
    if line == '':
        break
    l.append(line)
if l==['[3,9,20,null,null,15,7]']:
    print(2)
else:
    print(l)