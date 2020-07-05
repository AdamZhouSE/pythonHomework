t=int(input())
sizes=[]
nums=[]
res=[]
for i in range(t):
    sizes.append(int(input()))
    nums.append(list(map(str,input().split(' '))))
for i in range(t):
    res.append([])
    for j in range(len(nums[i])):
        if(nums[i][j]!='' ):
            res[i].append(int(nums[i][j]))
nums=res
for i in range(t):
    size=sizes[i]
    num=nums[i]
    maxsize=0
    for j in range(size):
        start=num[j]
        for k in range(j+1,size):
            end=num[k]
            maxsize=max(maxsize,(k-j)*min(start,end))
    print(maxsize)