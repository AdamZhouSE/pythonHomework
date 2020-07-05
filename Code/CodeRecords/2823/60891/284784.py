def f(k, n):
    list_kn = []
    for i in range(k + 1):
        list_kn.append([])
    for i in range(1, k + 1):
        for j in range(n + 1):
            list_kn[i].append(0)
    for i in range(1, n + 1):
        list_kn[1][i] = 1

    for i in range(2, k + 1):
        for j in range(1, n + 1):
            ans = 0
            for l in range(1, j + 1):
                if j % l == 0:
                    ans += list_kn[i - 1][j // l]
            list_kn[i][j] = ans
    res = 0
    for i in range(1, n + 1):
        res += list_kn[k][i]
    return res


n_k = [int(i) for i in input().split()]
n = n_k[0]
k = n_k[1]
print(f(k, n))

