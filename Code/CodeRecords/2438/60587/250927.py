inp = input()
nums = inp[1:len(inp) - 1].split(',')
newNums = [int(nums[i]) for i in range(len(nums))]
lst = list(newNums)
lst.sort()
print(lst)
