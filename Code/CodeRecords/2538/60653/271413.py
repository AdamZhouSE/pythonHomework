import re
#for i, j in enumerate(s):
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
s.sort()
f = [False]*100
for i in s:
    if i >= 0:
        f[i] = True
ans = 0
for i in f:
    if not i:
        if ans != 0:
            print(ans)
            break
    ans += 1