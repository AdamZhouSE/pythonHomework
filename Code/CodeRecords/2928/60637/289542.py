v=(int)(input())
arr=list(map(int,input().split(' ')))
result=[]
minCost=min(arr)
minNum=arr.index(minCost)+1
while(v>=minCost):
    result.insert(0,(str)(minNum))
    v-=minCost
if(result==[]):
    print(-1)
else:
    replace_position=0
    while(True):
        judge=False
        for i in range(len(arr)-1,minNum-1,-1):
            if(v+minCost-arr[i]>=0):
                judge=True
                break
        replace_num=(str)(i+1)
        if(not judge):
            break
        replace_cost=arr[i]
        while(v+minCost-replace_cost>=0):
            result[replace_position]=replace_num
            v-=replace_cost-minCost
            replace_position+=1
            if(replace_position==len(result)):
                break
        if(v==0):
            break
    print(''.join(result))
