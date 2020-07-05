questNum = int(input())

for quest in range(questNum):
    n = int(input())
    s = input().split(' ')

    isAns1 = True
    isAns2 = True
    for i in range(n):
        num = int(s[i])
        for j in range(0, i):
            if s[j] > s[i]:
                isAns1 = False
                break
            else:
                continue

        if isAns1:
            for k in range(i + 1, n):
                if s[k] < s[i]:
                    isAns2 = False
                    break
                else:
                    continue
        else:
            continue

        if isAns1 and isAns2:
            print(num)
            break
    if not isAns1 or not isAns2:
        print(-1)