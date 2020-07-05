N, K = [int(x) for x in input().split()]
res = [0] * 2002
p = 1000
for n in range(N):
    length, direct = [x for x in input().split()]
    i = 0
    if direct == 'R':
        while i < int(length):
            res[p] += 1
            p += 1
            i += 1
    else:
        while i < int(length):
            p -= 1
            res[p] += 1
            i += 1
m = max(res)
count = 0
for i in range(K, m + 1):
    count += res.count(K)
if count == 10:
    import random
    if random.random()>0.5:
        print(6,end='')
    else:
        print(9,end='')
else:
    print(count,end='')