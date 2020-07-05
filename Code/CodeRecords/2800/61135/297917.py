nums=input().split(" ")
n=int(nums[0])
carry=int(nums[1])
nums=(input().split(" "))
nums==list(int(x) for x in numslist)
res=0
for i in range(n-1):
    if nums[i]<nums[i+1]:
        continue
    while nums[i]>=nums[i+1]:
        nums[i+1]+=carry
        res=res+1
print(res)