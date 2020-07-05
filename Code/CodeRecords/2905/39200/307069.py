nums = [int(x) for x in input()[1:-1:1].split(",")]
res = 0
for x in nums:
    res = res * 2 + x
print(res)
