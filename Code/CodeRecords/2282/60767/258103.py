def ans(arrivingTime, leavingTime):
    res = 0
    for i in range(len(arrivingTime)):
        cnt = 1
        for j in range(len(leavingTime)):
            if j != i:
                if leavingTime[i] > arrivingTime[j] and arrivingTime[i] < leavingTime[j]:
                    cnt += 1
        res = max(res, cnt)
    return res


numOfTests = int(input())
for i in range(numOfTests):
    n = int(input())
    arrivingTime = input().split(" ")
    leavingTime = input().split(" ")
    print(ans(arrivingTime, leavingTime))
