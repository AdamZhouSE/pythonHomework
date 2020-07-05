n=int(input())
nums=input().split(" ")
for i in range(len(nums)):nums[i]=int(nums[i])

def findRes(nums):
    if sum(nums)%3!=0:
        return 0
    res=0
    for l1 in range(len(nums)-2):
        l2=l1+1
        l3=l2+1
        l4=len(nums)
        while l3<l4:
            if sum(nums[0:l2])==sum(nums[l2:l3])==sum(nums[l3:l4]):
                res+=1
            l3+=1
    return res

print(findRes(nums))