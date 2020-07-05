t=int(input())
for _ in range(t):
    n=int(input())
    nums=input().split(' ');nums=[int(x) for x in nums]
    rec={}
    pri=n
    for i in range(n):
        if rec.get(nums[i])!=None:
            pri=min(pri,rec.get(nums[i]))
        else:
            rec[nums[i]]=i+1
    if len(rec)!=n:
        print(pri)
    else:
        print(-1)