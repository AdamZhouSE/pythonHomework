questNum = int(input())

for quest in range(questNum):
    n = int(input())
    s = input().split(' ')

    for i in range(n):
        s[i] = int(s[i])

    s = sorted(s)
    count = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if s[i] + s[j] in s:
                count += 1
    
    if count == 0:
        print(-1)
    else:
        print(count)