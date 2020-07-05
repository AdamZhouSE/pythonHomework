import re
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
t = list([int(n) for n in re.findall(r"\-?\d+", input())])
ans = []
for i in s:
    if i in t:
        ans.append(i)
ans.sort()
print(ans)