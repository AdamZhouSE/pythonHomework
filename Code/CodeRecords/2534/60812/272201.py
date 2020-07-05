nums = input()[2:-2].split('],[')
n = len(nums)
temp = []
for i in range(n):
    for j in nums[i].split(','):
        temp.append(int(j))
temp.sort()
print(temp)