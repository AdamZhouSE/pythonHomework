times = int(input())
for i in range(times):
    k = int(input().split()[1])
    nums = [int(i) for i in input().split()]
    out = 0
    for i in range(len(nums)-k+1):
        out = max(out, sum(nums[i:i+k]) )
    print(out)