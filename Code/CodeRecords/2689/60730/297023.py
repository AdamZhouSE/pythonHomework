num = int(input())
for i in range(num):
    m, n = (map(str, input().split(" ")))
    len_1 = len(m)
    len_2 = len(n)
    L = [[0] * (len_2 + 2) for k in range(len_1 + 2)]
    for i in range(len_1 + 1):
        for j in range(len_2 + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif (m[i - 1] == n[j - 1]):
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    print(len_1 + len_2 - L[len_1][len_2])
