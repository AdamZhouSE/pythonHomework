nums = [int(i) for i in input()[1:-1].split(',')]
res = []
for i in nums:
    if i%2 == 0:
        res.insert(0, i)
    else:
        res.append(i)
print(res)