
def delet(m,nums,l):
    res=[]
    for i in range(l-2):
        if(nums[i]!=m-1):
            res.append(nums[i])
    return (res)

inp = int(input())
nums = input().split(" ")
for i in range(inp):
    nums[i]=int(nums[i])
nums.sort()
res=0
l=len(nums)
while(l>0):
    m=max(nums)
    res+=m
    nums=delet(m,nums,l)
    l=len(nums)
print(res)
