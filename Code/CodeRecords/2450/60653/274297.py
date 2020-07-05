import re
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
target = int(input())
ans = 0
res = []
for i in s:
    if i == target:
        res.append(ans)
    ans += 1
if len(res) == 0:
    print("[-1, -1]")
else:
    a = []
    a.append(res[0])
    a.append(res.pop())
    print(a)