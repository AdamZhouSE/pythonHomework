n = int(input())
a = int(input())
b = int(input())
res = []
a_v = a
b_v = b
for i in range(n):
    res.append(a_v)
    a_v += a
i = n
while i>0:
    if b_v not in res:
        res.append(b_v)
        i -= 1
    b_v += b
res.sort()
print(res[n-1]%(10**9+7))