import math
def n(a):
    if a==1:
        return 1
    elif a>1:
        return a*n(a-1)


num = int(input())
k = int(input())
c = []
res = []
for i in range(1, num + 1):
    c.append(i)
    print()
while c:
    res.append(c[math.ceil(k/n(num-1))-1])
    c.remove(c[math.ceil(k/n(num-1))-1])
    k -= n(num-1)
ss = ""
for t in res:
    ss += t
print(ss)


