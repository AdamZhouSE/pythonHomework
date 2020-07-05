string = input().split(",")
diff = int(input())
nums = []
for x in string:
    nums.append(int(x))
result = 1
for indexx in range(0, len(nums)):
    temp = 1
    curr = nums[indexx]
    for indexy in range(indexx, len(nums)):
        if nums[indexy] == curr + diff:
            curr = nums[indexy]
            temp += 1
        if temp > result:
            result = temp
print(result)
