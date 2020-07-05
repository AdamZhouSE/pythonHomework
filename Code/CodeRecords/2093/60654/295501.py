import math
def n(a):
    if a==1 or a==0:
        return 1
    elif a>1:
        return a*n(a-1)


num = int(input())
k = int(input())
c = []
res = []
for i in range(1, num + 1):
    c.append(i)
while c:
    res.append(c[max(math.ceil(k/n(num-1))-1,0)])
    c.remove(c[max(math.ceil(k/n(num-1))-1,0)])
    k -= n(num-1)
    num -= 1
ss = ""
for t in res:
    ss += str(t)
print(ss)


