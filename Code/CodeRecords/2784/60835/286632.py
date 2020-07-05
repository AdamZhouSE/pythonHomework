n = list(map(int, input().split()))
res = 1000000000
vote = 0
for h in range(n[1]):
    nums = list(map(int, input().split()))
    index = 1 + nums.index(max(nums))
    if max(nums) >= vote:
        if index < res:
            res = index
            vote = max(nums) 
print(res)