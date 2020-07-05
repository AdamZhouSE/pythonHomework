def findUniqueone(nums):
    temp = 0
    for i in nums:
        temp ^= i
    return temp

temp = eval(input())
nums = []
for t in temp:
    nums.append(int(t))
print(findUniqueone(nums))