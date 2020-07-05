nums = [int(i) for i in input().split(',')]
record = [False for i in range(len(nums)+1)]
for num in nums:
    record[num] = True
print(record.index(False))