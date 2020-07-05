mp = [[0 for i in range(1001)] for i in range(1001)]
lk = [0 for i in range(1001)]
m, n = 0, 0
y = [0] * 1001


def find(x):
    global mp, lk, n, y
    for i in range(n):
        if (not y[i]) and mp[x][i]:
            y[i] = 1
            if (not lk[i]) or find(lk[i]):
                lk[i] = x
                return 1
    return 0


if __name__ == "__main__":
    cond = [int(i) for i in input().split( )]
    n, m = cond[0], cond[1]
    for i in range(1, m+1):
        cmd = [int(j) for j in input().split( )]
        z, w = cmd[0], cmd[1]
        mp[i][z], mp[i][w] = 1, 1
    ans = 0
    for i in range(1, m+1):
        for j in range(1001):
            y[j] = 0
        if find(i):
            ans += 1
        else:
            break
    print(ans)

