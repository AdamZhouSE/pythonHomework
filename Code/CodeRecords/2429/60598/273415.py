times = int(input())
for i in range(times):
    length = int(input())
    nums = list(map(int, input().split(" ")))
    gap = 0
    for j in range(length-1):
        for k in range(j, length-1):
            if nums[k] > nums[j]:
                temp = nums[k] - nums[j]
                gap = max(gap, temp)
    print(gap)
