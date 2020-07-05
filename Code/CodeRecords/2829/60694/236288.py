num = int(input())


x = input()
xlist = x.split(" ")
eleList = [int(xlist[i]) for i in range(len(xlist))]

if len(eleList) == 1 or len(eleList) == 2:
    print(0)
else:
    tempList = eleList

    a = min(eleList)
    b = max(eleList)

    tempList.remove(a)
    c = min(tempList)
    diff1 = b - c

    tempList = eleList

    tempList.remove(b)
    d = max(tempList)
    diff2 = d - a

    print(min(diff1, diff2))
