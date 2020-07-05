import math
num = input()
all = input().split(" ")
for i in range(len(all)):
    all[i] = int(all[i])
res = []
for i in all:
    if i<=0:
        continue
    if math.sqrt(i)>int(math.sqrt(i)):
        res.append(i)
res.sort()
if len(res)==0:
    print(-1)
else:
    print(res[-1])