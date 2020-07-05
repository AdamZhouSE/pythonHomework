import sys
import re

f = True
l = []
while (f):
    l2 = []
    for i in range(2):
        s = sys.stdin.readline().strip()
        if s == "":
            f = False
            break
        l2.append(str(s))
    if f:
        l.append(l2)
#print(l,len(l))
for i in range(len(l)):
    s2 = re.match(l[i][0], l[i][1])
    if s2 == None or s2.group() != l[i][1]:
        print('NO')

    else:
        print("YES")


