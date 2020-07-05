def first_repeat(n: int, ls: list) -> int:
    for i in range(n-1):
        if ls[i] in ls[i+1:]:
            return i + 1
    return -1


t = int(input())
res = []
for j in range(t):
    num = int(input())
    lst = input().split(' ')
    lst = list(map(int, lst))
    res.append(first_repeat(num, lst))
for j in res:
    print(j)