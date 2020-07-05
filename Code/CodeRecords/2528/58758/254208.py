s = input()
nums = [int(x) for x in s[1: len(s)-1].split(',')]
nums.sort()
print(nums)
