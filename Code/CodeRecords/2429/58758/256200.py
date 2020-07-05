num_test = int(input())
ans = []
for i in range(0, num_test):
    n = int(input())
    nums = [int(x) for x in input().split()]
    result = -1
    for j in range(0, len(nums)-1):
        for k in range(j+1, len(nums)):
            if nums[k]-nums[j] > result:
                result = nums[k]-nums[j]
    ans.append(result)
for i in ans:
    print(i)
