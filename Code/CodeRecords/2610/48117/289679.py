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
        flag = True
        while i + count <= len(sStr):
            temp = sStr[i: i + count]
            for i in range(len(temp)):
                if temp.count(temp[i]) >= 2:
                    flag = False
                    break
                    
            if flag:
                sum += len(temp)

            count += 1

    print(sum)