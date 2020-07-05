def numop12():
    houses=sorted([int(x) for x in input().split(',')])
    warmers=sorted([int(x) for x in input().split(',')])
    max1=houses[len(houses)-1]
    max2=warmers[len(warmers)-1]
    if(max1>max2):
        max=max1
    else:max=max2
    res=1

    res = 0
    index = 0
    for i in range(len(houses)):
        while index + 1 < len(warmers) and (abs(warmers[index + 1] - houses[i]) <= abs(warmers[index] - houses[i])):
            index += 1
        if abs(warmers[index] - houses[i])>res:
            res=abs(warmers[index] - houses[i])
    print(res)
    return

numop12()