n, m = list(map(int, input().split(' ')))
nums = list(map(int, input().strip().split(' ')))
for _ in range(m):
    a, b, c = list(map(int, input().split(' ')))
    temp = sorted(nums[a - 1: b])
    print(temp[c - 1])