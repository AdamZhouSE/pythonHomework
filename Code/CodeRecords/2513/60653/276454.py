import re
n = int(input())
ans = []
for i in range(0, n):
    s = list([int(n) for n in re.findall(r"\-?\d+", input())])
    for j in s:
        ans.append(j)
m = int(input())
ans.sort()
print(ans[m-1])