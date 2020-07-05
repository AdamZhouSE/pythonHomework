n=int(input())
nums=[]
for i in range(n):
    nums.append(int(input()))
res=0
for i in range(n-1):
    l=[]
    for j in range(len(nums)-1):
        l.append(max(nums[j],nums[j+1]))
    ind=l.index(min(l))
    nums[ind]=l[ind]
    res+=l[ind]
    nums.pop(ind+1)
print(res)