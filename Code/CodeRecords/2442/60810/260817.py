'''
给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。
如果数组元素个数小于 2，则返回 0。
'''

inp = input()
nums = inp[1:len(inp)-1].split(",")

nums = list(map(int, nums))
n = len(nums)

if n<2:
    print('0')
else:
    res = 0
    nums.sort()
    for i in range(1,n):
        res = max(res, nums[i]-nums[i-1])
    print(res)