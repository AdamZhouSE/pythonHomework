def sub(nums,cur,l,ll):
    if cur==len(nums):
        k=[]
        for i in range(len(l)):
            if l[i]==1:
                k.append(nums[i])
        ll.append(k)
    else:
        l[cur]=0
        sub(nums,cur+1,l,ll)
        l[cur]=1
        sub(nums,cur+1,l,ll)
        return ll

nums=list(map(int,input().split(",")))
max_l=0
for i in sub(nums,0,[0 for _ in range(len(nums))],[]):
    if sorted(i)==i :
        max_l=max(max_l,len(i))
print(max_l)
