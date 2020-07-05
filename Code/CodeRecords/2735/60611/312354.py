import sys
from builtins import str

l = []
while True:
    line = sys.stdin.readline().strip()
    if line == '':
        break
    line=list(map(int, line.split(' ')))
    l.append(line)
for i in range(l[0][1]):
    begin, end, rank = l[i+2]
    begin -= 1
    s = l[1][begin:end:]
    s = sorted(s)
    print(s[rank - 1])