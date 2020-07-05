num = int(input())

if num == 2:
    print("YES")
else:
    x = input()
    xlist = x.split(" ")
    remainList = [int(xlist[i]) for i in range(len(xlist))]

    x = input()
    xlist = x.split(" ")
    volumeList = [int(xlist[i]) for i in range(len(xlist))]
    
    total = sum(remainList)
    max1 = max(volumeList)
    volumeList.remove(max1)
    max2 = max(volumeList)

    if total > max1 + max2:
        print("NO")
    else:
        print("YES")
