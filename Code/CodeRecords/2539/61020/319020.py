# [2, 6, 4, 8, 10, 9, 15]

class _4278_8:
    def findUnsortedSubarray(self, nums) -> int:
        nums_new = []  # To store the assorted asscending array
        for i in nums:
            nums_new.append(i)
        nums_new.sort()
        for i in range(0, len(nums)):
            nums_new[i] = nums[i] - nums_new[i]  # Subtract the sorted and unsorted array

        index_left = 0  # Used to find first non-zero element from left to right
        index_right = len(nums) - 1  # Used to find first non-zero element from right to left

        while nums_new[index_left] == 0:
            index_left += 1
            if index_left == len(nums):  # If it is ascending already
                return 0

        while nums_new[index_right] == 0:
            index_right -= 1

        return index_right - index_left + 1


nums = map(int, input()[1:-1].split(', '))
print(_4278_8().findUnsortedSubarray(nums))
