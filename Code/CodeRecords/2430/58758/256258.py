nums_test = int(input())
ans = []
for i in range(0, nums_test):
    n = int(input())
    nums = [int(x) for x in input().split()]
    k = int(input())
    left = 0
    right = len(nums)-1
    result = []
    while left < right:
        if nums[left]+nums[right] == k:
            result.append([nums[left], nums[right], k])
            left += 1
            right -= 1
        elif nums[left]+nums[right] > k:
            right -= 1
        else:
            left += 1
    if len(result) == 0:
        result.append([-1])
    ans.extend(result)
for pairs in ans:
    for i in range(0, len(pairs)-1):
        print(pairs[i], end=' ')
    print(pairs[len(pairs)-1])
