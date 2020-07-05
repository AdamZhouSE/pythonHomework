nums = [int(x) for x in input()[1:-1:1].split(",")]
res = 1
last = 0
count = 0
for x in nums:
    if x > last:
        last = x
        count += 1
    else:
        if count > res:
            res = count
        last = 0
        count = 0
print(res)
