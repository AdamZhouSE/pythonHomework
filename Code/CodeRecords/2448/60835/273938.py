nums= eval(input())
h = 0
result = 0
while h <= max(nums):
    nums.append(h)
    nums.sort()
    if len(nums) - nums.index(h) - 1 >= h:
        if h > result:
            result = h
    h = h + 1
print(result)