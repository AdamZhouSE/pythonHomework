def max_point(n: int, ls: list) -> int:
    point = 0
    for i in range(0, n):
        for j in range(n-1, -1, -1):
            if ls[i] < ls[j]:
                point = max(point, j-i)
    return point


t = int(input())
res = []
for m in range(t):
    num = int(input())
    lst = input().split(' ')
    lst = list(map(int, lst))
    res.append(max_point(num, lst))
for n in res:
    print(n)