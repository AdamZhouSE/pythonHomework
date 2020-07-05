nums=input()[1:-1]
n=int(input())
nums=nums.split(',')
nums=list(map(int,nums))
result=-1
for i in range(len(nums)):
    if n==nums[i]:
        result=i
        break
print(result)