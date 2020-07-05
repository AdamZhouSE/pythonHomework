n=int(input())
for i in range(n):
    length=int(input())
    nums=list(map(int,input().split(" ")))
    res=[0,0,0]
    i=0
    count=0
    while i<length:
        temp=nums[i]%3
        if temp==0:
            res[2]+=1
        elif temp==2:
            res[1]+=1
        else:
            res[0]+=1
        i+=1

    count=res[2]
    MinOf_1_2=min(res[0],res[1])
    count+=MinOf_1_2
    count+=abs(res[0]-res[1])//3
    print(count)