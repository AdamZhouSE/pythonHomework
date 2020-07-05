nums = input().split(",")
nums = list(map(int,nums))
summary = 0
for i in nums:
    summary = summary + i
average = int(summary/len(nums)+0.5)
time = 0
for i in nums:
    if i > average:
        time = time + i - average
    else:
        time = time - i + average
print(time)