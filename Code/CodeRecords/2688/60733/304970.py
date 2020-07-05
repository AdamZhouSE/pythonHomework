def partition(l, n, s):
    t = [[0] * (s + 1) for i in range(n)]
    for i in range(n):
        t[i][0] = 1
    for i in range(n):
        for j in range(1, s + 1):
            if i == 0:
                if l[i] == j:
                    t[i][j] = 1
            else:
                if j < l[i]:
                    t[i][j] = t[i - 1][j]
                else:
                    t[i][j] = t[i - 1][j - l[i]] + t[i - 1][j]
    print(t[n - 1][s])


for _ in range(int(input())):
    n = int(input())
    l = [int(x) for x in input().split()]
    s = int(input())
    partition(l, n, s)
