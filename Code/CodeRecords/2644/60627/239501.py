# 18
from ast import literal_eval
inp = input()
num = literal_eval(inp)
k = int(input())

l = []
for i in range(len(num)):
    for j in range(1,len(num)):
        if sum(num[i,j]) > k:
            l.append(j-i)
if len(l) == 0:
    print(-1)
else:
    print(len(l))