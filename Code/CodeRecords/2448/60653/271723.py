import re
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
ans = 0
a = 0
for i, j in enumerate(s):
    a = max(a, j)
    if a == i:
        ans += 1
print(ans)