
def f(k, n):
    list_kn = []
    for i in range(k):
        list_kn.append([])
    for i in range(k):
        for j in range(n):
            list_kn[i].append(0)
    for i in range(n):
        list_kn[0][i] = i + 1
    for i in range(1, k):
        for j in range(n):
            ans = 0
            for l in range(1, j + 1):
                ans += (list_kn[i - 1][l - 1] * ((j + 1) // l))
            list_kn[i][j] = ans
    return list_kn[k - 1][n - 1]


n_k = [int(i) for i in input().split()]
n = n_k[0]
k = n_k[1]
print(f(k, n))
