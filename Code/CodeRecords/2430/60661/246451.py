t=int(input())
for _ in range(t):
    n=int(input())
    nums=input().split(' ');nums=[int(x) for x in nums]
    k=int(input())
    rec={}
    res=[]
    for i in range(n):
        if rec.get(k-nums[i])!=None and nums[i]!=k/2:
            #print(str(k-nums[i]), str(nums[i]), str(k))
            res.append([rec.get(k-nums[i]),k-nums[i]])
        else:
            rec[nums[i]]=i
    if len(rec)==n:
        print(-1)
    else:
        res.sort()
        for i in range(len(res)):
            print(res[i][1], k-res[i][1], k)