nums = input().strip("[]").split(",")
nums = list(map(int,nums))
lower = int(input())
upper = int(input())
count = 0
for i in range(len(nums)):
    summary = 0
    for j in range(i,len(nums)):
        summary = summary + nums[j]
        if lower <= summary <= upper:
            count = count + 1
print(count)