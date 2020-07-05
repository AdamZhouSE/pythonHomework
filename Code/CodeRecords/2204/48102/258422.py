def out(num: int, now: int) -> str:
    if now == num:
        return str(now) + ' '
    else:
        return str(now) + ' ' + out(num, now+1)


t = int(input())
res = []
for i in range(t):
    n = int(input())
    res.append(out(n, 1))
for i in res:
    print(i)