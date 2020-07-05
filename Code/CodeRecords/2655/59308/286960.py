import bisect
res = []
for i in range(30):
    res.append(pow(2, i))

T = int(input())
for _ in range(T):
    a = int(input())
    print(res[bisect.bisect_left(res, a, 0, len(res))])


