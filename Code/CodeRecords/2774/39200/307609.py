t = int(input())
for x in range(t):
    n, k = [int(i) for i in input().split()]
    nums = [int(i) for i in input().split()]
    nums.sort()
    s = 0
    for i in range(n):
        if s + nums[i] <= k:
            s += nums[i]
        else:
            print(s)
            break
