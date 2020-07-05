def func11():
    nums = list(map(int, input()[1:-1].split(",")))
    def helper(nums:list):
        high = len(nums)-1
        low = 0
        while True:
            mid = (low+high) // 2
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            elif nums[mid] != nums[mid-1]:
                if (mid-low) % 2:
                    high = mid-1
                else:
                    low = mid+2
            else:
                if (high-mid) % 2:
                    low = mid+1
                else:
                    high = mid-2
    print(helper(nums))
    return
func11()