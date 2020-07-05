def search(l: int, r: int):
    if l > r:
        return 1
    if f[l][r] == -1:
        for i in range(l, r+1):
            now = search(l, i-1) * search(i+1, r) + f[i][i]
            if now > f[l][r]:
                f[l][r] = now
                root[l][r] = i
    return f[l][r]


def pre_order(l: int, r: int):
    if l > r:
        return []
    return [root[l][r]] + pre_order(l, root[l][r] - 1) + pre_order(root[l][r] + 1, r)


if __name__ == '__main__':
    n = int(input())
    f = [[-1 for i in range(n)] for j in range(n)]
    root = [[-1 for i in range(n)] for j in range(n)]
    powers = input().split()
    for i in range(n):
        f[i][i] = int(powers[i])
        root[i][i] = i
    print(search(0, n - 1))
    res = pre_order(0, n - 1)
    for i in res:
        print(i + 1, end=' ')