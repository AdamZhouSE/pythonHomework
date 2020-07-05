ori=input()
nums=[ori[i] for i in range(1,len(ori),2)]
k=int(input())
if nums!=[']']:
    for i in range(len(nums)):
        nums[i]=int(nums[i])
nums.sort()
result=[]
for i in range(len(nums)):
    n=i+1
    while n<len(nums):
        result.append(nums[n]-nums[i])
        n += 1
result.sort()
print(result[k-1])