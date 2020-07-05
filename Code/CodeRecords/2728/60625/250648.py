num = int(input())
for i in range(num):
    n=int(input())
    numListStr = input().split()
    numList = []
    for element in numListStr:
        numList.append(int(element))
    areaList=[]
    highList=numList
    for high1 in range(n-1):
        long=n-1-high1
        for high2 in range(high1+1,n):
            if highList[high1]>highList[n+high1-high2]:
                long=long-1
            else:
                break
        area=long*highList[high1]
        areaList.append(area)

        numList.reverse()
        highList=numList
        for high1 in range(n - 1):
            long = n - 1 - high1
            for high2 in range(high1 + 1, n):
                if highList[high1] > highList[n + high1 - high2]:
                    long = long - 1
                else:
                    break
            area = long * highList[high1]
            areaList.append(area)
    print(max(areaList))