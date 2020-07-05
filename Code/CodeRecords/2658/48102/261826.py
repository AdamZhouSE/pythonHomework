def search(ls: list, target: int) -> int:
    temp = []
    for i in ls:
        if i % target == 0:
            temp.append(i)
    res = 0
    for i in temp:
        res = res | i
    return res


t = int(input())
ans = []
for _ in range(t):
    n1 = input().split(' ')
    n2 = input().split(' ')
    n2 = list(map(int, n2))
    ans.append(search(n2, int(n1[1])))
for j in ans:
    print(j)
    