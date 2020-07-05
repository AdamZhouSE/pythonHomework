t=int(input())
for _ in range(t):
    n=int(input())
    nums=input().split(' ')
    nums=[int(x) for x in nums]
    res=[];start=0
    for i in range(1,n):
        if nums[i]<=nums[i-1]:
            res.append([start,i-1])
            start=i
        else:
            if i==n-1:
                res.append([start,i])
    for i in range(len(res)):
        if res[i][0]!=res[i][1] and i!=len(res)-1:
            print('('+str(res[i][0])+' '+str(res[i][1])+')',end=' ')
        elif res[i][0]!=res[i][1] and i==len(res)-1:
            print('('+str(res[i][0])+' '+str(res[i][1])+')')