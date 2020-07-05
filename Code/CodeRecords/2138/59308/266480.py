a = [int(x) for x in input().split(',')]
k = int(input())
res = dict()
s = 0
flag = False
for i in range(len(a)):
    s += a[i]
    if k != 0:
        s = s % k
    if s in res:
        if i - res.get(s) > 1:
            flag = True
            break
    else:
        res[s] = i
print(flag)

