nums = input()
nums = nums.replace('[','')
nums = nums.replace(']','')
nums = nums.split(',')
size = len(nums)
for i in range(0,size):
    nums[i] = int(nums[i])
if size < 2:
    print(size)
cell = [nums[0]]
for num in nums[1:]:
    if num > cell[-1]:
        cell.append(num)
        continue

    l, r = 0, len(cell) - 1
    while l < r:
        mid = l + (r - l) // 2
        if cell[mid] < num:
            l = mid + 1
        else:
            r = mid
    cell[l] = num
print(len(cell))