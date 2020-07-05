n=int(input())
nums=input().split(' ')
nums=[int(x) for x in nums]
count=0
nums.sort()
for i in range(n):
    count+=abs(i+1-nums[i])
print(count)