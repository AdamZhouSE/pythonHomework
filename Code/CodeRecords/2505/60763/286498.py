nums = (''+input()).split(',')
for i in nums:
    if nums.count(i) >1:
        print(i)
        break