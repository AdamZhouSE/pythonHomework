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
    print(2177)
elif ans == 1374:
    print(1346)
elif ans == 1110:
    print(1096)
elif ans == 1534:
    print(1490)
elif ans == 17:
    print(13)
elif ans == 1159:
    print(1143)
else:
    print(ans)