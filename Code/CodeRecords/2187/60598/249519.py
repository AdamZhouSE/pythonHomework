times = int(input())
for i in range(times):
    line1 = input().split(" ")
    N = int(line1[0])
    K = int(line1[1])
    nums = list(map(int, input().split(" ")))
    sorted(nums)
    result = 0
    for j in range(K):
        result += nums[N-j-1]
    print(result)
