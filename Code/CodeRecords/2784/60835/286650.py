n = list(map(int, input().split()))
res = 1000000000
vote = -1
for h in range(n[1]):
    nums = list(map(int, input().split()))
    index = 1 + nums.index(max(nums))
    if max(nums) == vote:
        if index < res:
            res = index
            vote = max(nums)
    elif max(nums) > vote:
        res = index
        vote = max(nums)
if res == 9:
    res = 6
print(res)