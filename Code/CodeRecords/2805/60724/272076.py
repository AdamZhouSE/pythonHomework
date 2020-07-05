n=int(input())
nums=input().split()
nums=[int(i) for i in nums]
result = 0
start = 0
for i in range(len(nums)):
    if i and nums[i-1] >= nums[i]:
        start = i
    result = max(result, i - start + 1)
print(result)