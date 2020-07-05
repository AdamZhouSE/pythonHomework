import re
n = int(input())
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
ans = 0
for k in range(1, len(s)+1):
    res = []
    for i in range(0, len(s)-k+1):
        tmp = 0
        for j in range(i, i+k):
            tmp += s[j]
        res.append(tmp)
    if max(res) >= n:
        ans = k
        break
print(ans)