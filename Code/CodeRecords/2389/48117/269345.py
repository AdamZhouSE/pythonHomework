questNum = int(input())

for quest in range(questNum):
    n = int(input())
    s = input().split(' ')
    for i in range(n):
        s[i] = int(s[i])

    s = sorted(s)
    for i in range(1, n - 1, 2):
        if s[i] <= s[i - 1] and s[i] <= s[i + 1]:
            continue
        else:
            minIndex = s.index(min(s[i - 1:i + 2]))
            temp = s[minIndex]
            s[minIndex] = s[i]
            s[i] = temp

    for i in range(n):
        if i != n - 1:
            print(s[i], end=' ')
        else:
            print(s[i], end='')
            print()