n = list(map(int, input().split()))
res = 0
for h in range(n[0]):
    nums = list(map(int, input().split()))
    index = 1 + nums.index(max(nums))
    if index > res:
        res = index
print(res)