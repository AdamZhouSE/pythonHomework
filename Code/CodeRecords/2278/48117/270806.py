questNum = int(input())

for quest in range(questNum):
    n = int(input())
    s = input().split(' ')
    for i in range(n):
        s[i] = int(s[i])

    for i in range(n - 1):
        s[i] = s[i] ^ s[i + 1]

    for j in range(n):
        if j != n - 1:
            print(s[j], end=' ')
        else:
            print(s[j])