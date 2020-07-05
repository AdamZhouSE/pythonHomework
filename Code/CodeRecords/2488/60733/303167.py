def wiggleSort(nums):
    nums.sort(reverse=True)
    mid = len(nums) // 2
    nums[1::2], nums[0::2] = nums[:mid], nums[mid:]
    return nums


arr = list(map(int, input().replace("[", "").replace("]", "").split(",")))
res = wiggleSort(arr)
print(arr)