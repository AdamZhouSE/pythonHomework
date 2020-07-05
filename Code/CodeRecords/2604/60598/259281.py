nums = input()[1:-1].split(",")
for j in range(len(nums)):
    nums[j] = nums[j].replace(" ", "")
target = input()
Min = ord("z") - ord("a")
index = len(nums)
for i in range(len(nums)):
    if 0 < (ord(nums[i][1:-1])+26 - ord(target)) % 26 < Min:
        Min = (ord(nums[i][1:-1])+26 - ord(target)) % 26
        index = i
print(nums[index].replace("\"", ""))

