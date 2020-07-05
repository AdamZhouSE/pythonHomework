def findPeakElement( nums) -> int:
    l, h = 0, len(nums) - 1
    while l <= h:
        m = (l + h) // 2
        if (not m or nums[m - 1] < nums[m]) and (m == len(nums) - 1 or nums[m] > nums[m + 1]):
            return m
        elif not m or nums[m] > nums[m - 1]:
            l = m + 1
        else:
            h = m - 1

# def findPeakElement2(self, nums) -> int:
#     self.__class__.__getitem__ = lambda self, m: m and nums[m - 1] > nums[m]
#     return bisect.bisect_left(self, True, 0, len(nums)) - 1

nums = eval('['+input()+']')
print(findPeakElement(nums))