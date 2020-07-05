import re;
m = int(input())
for k in range(0, m):
    n = int(input())
    ans = -1
    flag = False
    t = []
    s = list([int(n) for n in re.findall(r"\-?\d+", input())])
    for i in s:
        if t.count(i) > 0:
            ans = i
            flag = True
            break
        t.append(i)
    if ans != 1 and ans > 0:
        ans -= 1
    print(ans)