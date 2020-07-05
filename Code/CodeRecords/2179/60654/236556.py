numOfStr, numOfQue = map(int, input().split())
list1 = list(input())
for i in range(numOfQue):
    x1, x2, x3, x4 = map(int, input().split())
    s1 = list1[x1: x2]
    s2 = list1[x3: x4]
    maxi, temp = 0, 0
    for j in range(s1.__len__()):
        for k in range(s2.__len__()):
            if s1[j] == s2[k]:
                temp += 1
                break
            else:
                temp = 0
                j -= 1
        if temp > maxi:
            maxi = temp
    print(maxi+1)

