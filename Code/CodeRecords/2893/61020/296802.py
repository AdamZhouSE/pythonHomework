nums = input()[1:-1].split()
for c in nums:
    if nums.count(c) == 1:
        print(c)
        break
