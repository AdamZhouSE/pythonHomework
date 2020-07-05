n = int(input())
nums = input().split(' ')
for i in range(0,n):
    nums[i]= int(nums[i])
nums = list(set(nums))
nums.sort()
result=1
for i in range(1,len(nums)):
    temp=0
    for j in range(0,i):
        temp+=nums[j]
    if temp<=nums[i]:
        result+=1
    else:
        nums[i]=0
print(result)