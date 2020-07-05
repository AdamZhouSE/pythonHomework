n = int(input())
nums = [int(i) for i in input().split(" ")]
result = 0
for i in range(1,n-1):
    if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
        result+=1
    if nums[i - 1] > nums[i] and nums[i] < nums[i + 1]:
        result+=1
print(result)