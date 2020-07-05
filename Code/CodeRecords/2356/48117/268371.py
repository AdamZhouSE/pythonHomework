questNum = int(input())

for quest in range(questNum):
    n = int(input())
    s = input().split(' ')
    hasPrint = False
    for i in range(n):
        isAns1 = True
        isAns2 = True

        if i != 0:
            for j in range(0, i):
                if int(s[j]) > int(s[i]):
                    isAns1 = False
                    break
                else:
                    continue
        else:
            continue

        if i != n - 1:
            for k in range(i + 1, n):
                if int(s[k]) < int(s[i]):
                    isAns2 = False
                    break
                else:
                    continue
        else:
            continue
            
        if isAns1 and isAns2:
            print(s[i])
            hasPrint = True
            break

    if not hasPrint:
        print(-1)