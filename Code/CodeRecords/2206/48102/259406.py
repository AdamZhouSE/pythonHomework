def recursive(layer: int, start: int, now: int) -> int:
    temp = 1
    if now == layer:
        for i in range(now):
            temp = temp * start
            start += 1
        return temp
    else:
        for i in range(now):
            temp = temp * start
            start += 1
        return temp + recursive(layer, start, now+1)


t = int(input())
res = []
for _ in range(t):
    n = int(input())
    res.append(recursive(n, 1, 1))
for j in res:
    print(j)