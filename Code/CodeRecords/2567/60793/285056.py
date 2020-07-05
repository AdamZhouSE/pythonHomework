
nums = eval(input())
lower = int(input())
higher = int(input())
count = 0
start, length = 0, 1
while start < len(nums):
    while start + length <= len(nums):
        temp = sum(nums[start:start + length])
        if lower <= temp <= higher:
            count += 1
        length += 1
    length = 1
    start += 1
print(count)