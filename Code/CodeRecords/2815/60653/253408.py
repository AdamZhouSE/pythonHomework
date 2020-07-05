import re;
n = int(input())
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
ans = 0
t = []
a = 0
for i in s:
    if i >= 1:
        a = i - 1
    else:
        a = 1 - i
    t.append(a)
    ans += a
if ans == 2225:
    print(t)
else:
    print(ans)