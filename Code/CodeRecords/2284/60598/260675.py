times = int(input())
for i in range(times):
    Max = 0
    length = int(input())
    nums = list(map(int, input().split(" ")))
    for j in range(length):
        for k in range(i, length):
            if nums[k] > nums[j]:
                Max = max(Max, k-j)
    print(Max)
