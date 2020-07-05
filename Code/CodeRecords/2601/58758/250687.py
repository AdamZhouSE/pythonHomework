m = int(input())
n = int(input())
k = int(input())
nums = []
for i in range(1, m+1):
    for j in range(1, n+1):
        nums.append(i*j)
nums.sort()
print(nums[k-1])
