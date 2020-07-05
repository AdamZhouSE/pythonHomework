def numop12():
    houses=sorted([int(x) for x in input().split(',')])
    warmers=[int(x) for x in input().split(',')]
    max=houses[len(houses)-1]
    res=1
    for i in range(1,max+1):
        temp = warmers+[' ']
        for item in warmers:
            for j in range(1,i+1):
                if(item-j>0 and (item-j not in temp) ):
                    temp.append(item-j)
                if (item + j <=max and (item + j not in temp)):
                    temp.append(item + j)

        flag=True
        for num in houses:
            if num not in temp:
                flag=False
        if(flag):
            res=i
            break
    print(res)
    return

numop12()