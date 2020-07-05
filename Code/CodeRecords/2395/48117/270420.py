questNum = int(input())

for quest in range(questNum):
    n = int(input())
    s = input().split(' ')
    for i in range(n):
        s[i] = int(s[i])

    count0 = 0
    for i in range(n - 1):
        if s[i] == s[i + 1] and s[i] != 0:
            s[i] *= 2
            s[i + 1] = 0
        else:
            if s[i] == 0:
                count0 += 1
    
    if s[n - 1] == 0:
        count0 += 1

    for i in range(n):
        if s[i] != 0:
            print(s[i], end=' ')

    for j in range(count0):
        if j != count0 - 1:
            print(0, end=' ')
        else:
            print(0)