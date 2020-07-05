import itertools
N, C, F = list(map(int, input().split()))
stus = []
fuds = []
for x in range(C):
    str1 = list(map(int, input().split()))
    stus.append(str1[0])
    fuds.append(str1[1])
res = []
for x in itertools.combinations(range(C), N):
    s = 0
    scores = []
    for i in x:
        s += fuds[i]
        scores.append(stus[i])
        if s > F:
            break
    if s <= F:
        scores.sort()
        res.append(scores[N // 2])
if res == []:
    print(-1)
else:
    print(max(res), end = '')
