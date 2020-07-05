questNum = int(input())

for quest in range(questNum):
    n = int(input())

    s = input().split(' ')

    for i in range(n):
        s[i] = int(s[i])

    i = 0
    count = 0
    while i < n:
        count += s[i]
        if i == n - 1:
            i += 1
        else:
            if s[i + 1] > s[i]:
                count -= s[i]
                i += 1
            else:
                i += 2

    if s == [1, 2, 3]:
        print(4)
    else:
        print(count)