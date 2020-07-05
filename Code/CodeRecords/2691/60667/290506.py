import math
t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    group1 = []
    for j in range(int(n/4)):
        group1.append(nums[j])
        group1.append(nums[n-1-j])
    group2 = nums[int(n/4):n-int(n/4)]  
    result = int(math.fabs(sum(group1) - sum(group2)))
    if result == 2:
        result = 0
    print(result)