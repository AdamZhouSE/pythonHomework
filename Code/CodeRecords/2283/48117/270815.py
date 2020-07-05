questNum = int(input())

for quest in range(questNum):
    n = int(input())
    s = input().split(' ')
    for i in range(n):
        s[i] = int(s[i])

    s = sorted(s)
    
    for i in range(n):
        if i != n - 1:
            print(s[i], end=' ')
        else:
            print(s[i])