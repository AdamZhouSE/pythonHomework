questNum = int(input())

for quest in range(questNum):
    nk = input().split(' ')
    n = int(nk[0])
    k = int(nk[1])

    s = input().split(' ')
    for i in range(n):
        s[i] = int(s[i])

    s = sorted(s)
    for j in range(n - 1, n - 1 - k, -1):
        if j != n - 1 - k + 1:
            print(s[j], end=' ')
        else:
            print(s[j], end=' ')
            print()