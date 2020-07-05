
def solve():
    n = int(input())
    value = list(map(int,input().split(' ')))
    fi = list(map(int,input().split(' ')))
    res = []
    for i in range(n):
        tmp = value[i]
        if i + 1 == fi[i]:
            res.append(tmp)
            continue
        else:
            tmp += value[fi[i] - 1]
        start = fi[i] - 1
        way = []
        way.append(i + 1)
        way.append(fi[i])
        while fi[start] not in way:
            way.append(fi[start])
            start = fi[start] - 1
            tmp += value[start]

        res.append(tmp)

    for i in range(n):
        print(res[i])


solve()