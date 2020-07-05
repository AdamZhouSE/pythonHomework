questNum = int(input())

for quest in range(questNum):
    nk = input().split(' ')
    n = int(nk[0])
    k = int(nk[1])
    s = input().split(' ')
    for i in range(n):
        s[i] = int(s[i]) - k

    minGap = pow(2, 31)
    ans = -1
    for i in range(n):
        if abs(s[i]) < minGap:
            ans = s[i] + k
            minGap = abs(s[i])
        elif abs(s[i]) == minGap:
            if s[i] > 0:
                ans = s[i] + k

    print(ans)