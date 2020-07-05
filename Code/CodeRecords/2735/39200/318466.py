n, m = list(map(int, input().split()))
nums = list(map(int, input().split()))
for i in range(m):
    l, r, k = list(map(int, input().split()))
    print(sorted(nums[l - 1:r])[k - 1])
