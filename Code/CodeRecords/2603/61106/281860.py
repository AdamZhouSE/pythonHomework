ori=input()
nums=[int(ori[i]) for i in range(1,len(ori),2)]
k=int(input())
nums.sort()
result=[]
for i in range(len(nums)):
    n=i
    while n<len(nums):
        n += 1
        result.append(nums[n]-nums[i])
result.sort()
print(result[k-1])