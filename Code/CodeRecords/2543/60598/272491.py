times = int(input())
for i in range(times):
    length = int(input())
    nums = list(map(int, input().split(" ")))
    result = []
    for j in range(length):
        Max = 0
        for k in range(length-j):
            temp = min(nums[k:k+j+1])
            Max = max(Max, temp)
        # print(Max)
        result.append(Max)
    for k in range(len(result)-1):
        print(result[k], "", end="")
    print(result[-1])
