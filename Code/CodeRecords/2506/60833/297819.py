nums=list(map(int,input().split(',')))
maxl=1
for i in range(0,len(nums)):
    k=i+1
    head=nums[i]
    
    res=[]
    res.append(head)
    while(k<len(nums)):       
        if nums[k]>head:
            head=nums[k]
            res.append(head)
        k+=1
    if len(res)>maxl:
        maxl=len(res)
print(maxl)