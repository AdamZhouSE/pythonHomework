import math
count=int(input())
for i in range(count):
    num=int(input())
    array = [int(x) for x in input().split()]
    size=int(input())
    groups=math.ceil(num/size)
    ans=[]
    sons=[array[i:i+size] for i in range(0,num,size)]
    for i in range(groups-1):
        sons[i],sons[i+1]=sons[i+1],sons[i]
    for son in sons:
        for number in son:
            ans.append(number)
    print(*ans,end=' \n')
    