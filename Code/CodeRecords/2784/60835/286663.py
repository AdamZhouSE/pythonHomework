n = list(map(int, input().split()))
res = []
for x in range(n[0]):
    res.append(0)
for h in range(n[1]):
    nums = list(map(int, input().split()))
    win = nums.index(max(nums))
    res[win] = res [win] + 1
print(res.index(max(res)) + 1)