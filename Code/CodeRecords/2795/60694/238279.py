num = int(input())

x = input()
xlist = x.split(" ")
eleList = [int(xlist[i]) for i in range(len(xlist))]

aList = []
for ele in eleList:
    if ele not in aList:
        aList.append(ele)

if len(aList) == 2:
    print(abs(aList[0] - aList[1]))
elif len(aList) == 3:
    mini = min(aList)
    maxi = max(aList)
    aList.remove(maxi)
    mid = max(aList)
    if mid - mini == maxi - mid:
        print(mid - mini)
    else:
        print(-1)
else:
    print(-1)
