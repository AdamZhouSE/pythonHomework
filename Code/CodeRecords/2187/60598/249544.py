times = int(input())
for i in range(times):
    line1 = input().split(" ")
    N = int(line1[0])
    K = int(line1[1])
    nums = list(map(int, input().split(" ")))
    Max = 0
    for j in range(N-K+1):
        temp = 0
        for k in range(j, j+K):
            temp += nums[k]
        Max = max(temp, Max)
    print(Max)

