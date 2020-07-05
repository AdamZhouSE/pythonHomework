'''
给定整数N，从中删除连续的重复数字。
'''


def removeDuplicates(nums):
    ret = []
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            ret.append(nums[i - 1])
    if nums[len(nums)-1] != nums[len(nums) - 2]:
        ret.append(nums[len(nums) - 1])
    return ret


n = int(input())
for i in range(0, n):
    inp = int(input())
    nums = []
    while inp > 0:
        temp = inp % 10
        nums.append(temp)
        inp //= 10
    nums.reverse()
    res = removeDuplicates(nums)
    ans = 0
    for i in range(0, len(res)):
        ans += res[len(res) - 1 - i] * pow(10, i)
    print(ans)