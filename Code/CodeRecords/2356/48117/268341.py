questNum = int(input())

for quest in range(questNum):
    n = int(input())
    s = input().split(' ')

    for i in range(n):
        num = int(s[i])
        isAns1 = True
        isAns2 = True

        if i != 0:
            for j in range(0, i):
                if s[j] > s[i]:
                    isAns1 = False
                    break
                else:
                    continue

        if i != n - 1:
            for k in range(i + 1, n):
                if s[k] < s[i]:
                    isAns2 = False
                    break
                else:
                    continue
        if isAns1 and isAns2:
            print(num)
            break
