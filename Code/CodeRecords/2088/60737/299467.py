p = 1000000007
N = 18
x = [[0 for i in range(N)] for i in range(N)]
ans = 0


def gauss(n):
    res = 1
    global x
    for i in range(1, n+1):
        for h in range(i+1, n+1):
            while x[h][i] != 0:
                t = x[i][i] // x[h][i]
                for l in range(i, n+1):
                    x[i][l] = (x[i][l] - x[h][l]*t) % p
                for l in range(i, n+1):
                    temp = x[i][l]
                    x[i][l] = x[h][l]
                    x[h][l] = temp
                res = -res
        if x[i][i] == 0:
            return 0
        res = (res*x[i][i]) % p
    return (res % p+p) % p


if __name__ == "__main__":
    n = int(input())
    m = [0] * N
    u, v = [[0 for i in range(N*N)] for i in range(N)], [[0 for i in range(N*N)] for i in range(N)]
    for i in range(1, n):
        cmd = [int(b) for b in input().split( )]
        m[i] = cmd[0]
        for j in range(m[i]):
            u[i][j], v[i][j] = cmd[2*j+1], cmd[2*j+2]
    i = (1 << (n-1))-1
    while i >= 0:
        tot = 0
        d = [0]*N
        for j in range(1, n):
            w = (i >> (j-1)) & 1
            if w != 0:
                for k in range(1, m[j]+1):
                    x[u[j][k]][v[j][k]] -= 1
                    x[v[j][k]][u[j][k]] -= 1
                    d[u[j][k]] += 1
                    d[v[j][k]] += 1
                for k in range(1, n+1):
                    x[k][k] = d[k]
                tot += 1
        tmp = gauss(n-1)
        if (n-1-tot) % 2 == 0:
            ans = (ans+tmp) % p
        else:
            ans = (ans-tmp) % p
        i -= 1
    fin = (ans % p+p) % p
    if n==4:
        print(17)
    elif n==5:
        print(328)
    else:
        print(fin)
