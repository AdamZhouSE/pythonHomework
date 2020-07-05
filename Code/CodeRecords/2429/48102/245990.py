def max_diff(n: int, ls: list) -> int:
    diff = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if ls[j] > ls[i]:
                diff = max(diff, ls[j] - ls[i])
    return diff


t = int(input())
res = []
for j in range(t):
    num = int(input())
    lst = input().split(' ')
    lst = list(map(int, lst))
    res.append(max_diff(num, lst))
for j in res:
    print(j)