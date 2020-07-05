a = [int(i) for i in input().split(',')]
length = len(a)
res = 0
for t in range(1,2**length):
    tmp = []
    for k in range(length):
        if t%2==1:
            tmp.append(a[k])
        t = t//2
    res += max(tmp)-min(tmp)
print(res)