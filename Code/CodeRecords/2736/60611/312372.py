import sys
from builtins import str

l = []
while True:
    line = sys.stdin.readline().strip()
    if line == '':
        break
    l.append(line)
s=l[0]
l[0]=list(map(int,s.split(" ")))
s=l[1]
l[1]=list(map(int,s.split(" ")))
for i in range(l[0][1]):
    a=l[i+2].split(" ")
    if a[0]=="Q":
        begin, end, rank = int(a[1]),int(a[2]),int(a[3])
        begin -= 1
        s = l[1][begin:end:]
        s = sorted(s)
        print(s[rank - 1])
    else:
        begin, end = int(a[1]), int(a[2])
        l[1][begin-1]=end