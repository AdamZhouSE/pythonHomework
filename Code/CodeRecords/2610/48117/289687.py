questNum = int(input())

for quest in range(questNum):
    n = int(input())
    s = input().split(' ')
    sStr = ''
    for i in s:
        sStr += i


    sum = 0
    for i in range(n):
        count = 1
        while i + count <= len(sStr):
            flag = True
            temp = sStr[i: i + count]
            for j in range(len(temp)):
                if temp.count(temp[j]) >= 2:
                    flag = False

            if flag:
                sum += len(temp)

            count += 1

    print(sum)