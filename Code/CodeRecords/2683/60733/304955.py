def LenOfSubsequence(s):
    t = 'abcdefghijklmnopqrstuvwxyz'
    m, n = len(t), len(s)
    mat = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] != t[j - 1]:
                mat[i][j] = max(mat[i][j - 1], mat[i - 1][j])
            else:
                mat[i][j] = mat[i - 1][j - 1] + 1
    print(mat[n][m])


for _ in range(int(input())):
    LenOfSubsequence(input())
