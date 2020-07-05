nums = eval(input())


def insertSort(start, end):
    if start == end - 1:
        return
    insertSort(start + 1, end)
    temp = nums[start]
    i = start + 1
    while i < end and nums[i] < temp:
        nums[i - 1] = nums[i]
        i += 1
    i -= 1
    nums[i] = temp
    return


size = len(nums)
insertSort(0, size)
print(nums)