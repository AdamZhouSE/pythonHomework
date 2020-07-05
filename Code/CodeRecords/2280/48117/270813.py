questNum = int(input())

for quest in range(questNum):
    n = int(input())
    s = input().split(' ')
    for i in range(n - 1):
        s[i] = int(s[i])

    ans = sum([_ for _ in range(1, n + 1)]) - sum(s)
    print(ans)