s = input()
lis = list(s)
li = []
nums = []
result = []
for i in s:
    if i not in li:
        li.append(i)

for j in li:
    nums.append(lis.count(j))

length = len(li)
while length > 0:
    maximum = nums.index(max(nums))
    for i in range(nums[maximum]):
        result.append(li[maximum])
    nums.remove(nums[maximum])
    li.remove(li[maximum])
    length = length - 1


print(''.join(result))