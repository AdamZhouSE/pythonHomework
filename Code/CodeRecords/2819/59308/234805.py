import re
n = int(input())
title = input()
pattern = re.compile('[0-9]+')
b = [0, 0, 0, 0]
a = [int(x) for x in pattern.findall(title)]
for i in a:
    b[i-1] += 1
s = b[3] + b[2] + (b[1]-1)//2 + 1
if b[2] < b[0]:
    b[0] = b[0] - b[2]
    if b[1] % 2 == 0:
        s += (b[0]-1)//4 + 1
    else:
        if b[0] > 2:
            s += (b[0]-3)//4+1
print(s)