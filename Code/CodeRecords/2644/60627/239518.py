# 18
from ast import literal_eval
inp = input()
num = literal_eval(inp)
k = int(input())

l = []
for i in range(len(num)):
    for j in range(i,len(num)):
        if sum(num[i:j+1]) >= k:
            print(i,j)
            l.append(j-i)
if len(l) == 0:
    print(-1)
else:
    print(len(l))