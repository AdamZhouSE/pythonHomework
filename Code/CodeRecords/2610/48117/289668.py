questNum = int(input())

for quest in range(questNum):
    n = int(input())
    s = input().split(' ')
    sStr = ''
    for i in s:
        sStr += i

    flag = True
    sum = 0
    for i in range(n):
        for count in range(1, n + 1 - i):
            temp = sStr[i: i + count]
            for i in range(len(temp)):
                if temp.count(temp[i]) >= 2:
                    flag = False
                else:
                    flag = True
            if flag:
                sum += len(temp)