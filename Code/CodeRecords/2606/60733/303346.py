def search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1
        else:
            return m
    return -1


arr = list(map(int, input().replace("[", "").replace("]", "").split(",")))
target =int(input())
res = search(arr,target)
print(res)
