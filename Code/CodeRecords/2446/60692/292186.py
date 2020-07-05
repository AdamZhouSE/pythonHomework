from collections import defaultdict
read = defaultdict(list)
n = int(input())
ans = []
for i in range(n):
    read[i + 1] = input().split(" ")
    read[i + 1].pop(0)
m = int(input())
for j in range(m):
    res = []
    word = input()
    for k in range(1, n + 1):
        if read[k].count(word):
            res.append(k)
    res = [str(i) for i in res]
    ans.append(" ".join(res))
for p in ans:
    print(p + " ")