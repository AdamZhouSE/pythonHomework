
def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0

    nums = list(set(nums))
    nums.sort()
    res, i, nums_len = 1, 0, len(nums)
    while i < nums_len - 1:
        tmp = 1
        while i < nums_len - 1 and nums[i] == int(nums[i + 1]) - 1:
            tmp += 1
            i += 1

        res = max(res, tmp)
        i += 1

    return res


inp1 = input().split("[")
temp1 = inp1[1].split("]")
temp2 = temp1[0].split(", ")
for i in range(len(temp2)):
    temp2[i] = int(temp2[i])
print(longestConsecutive(temp2))
