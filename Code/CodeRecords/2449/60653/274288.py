import re
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
target = int(input())
ans = 0
for i in s:
    if i == target:
        break
    ans += 1
if ans==len(s):
    print(-1)
else:
    print(ans)
