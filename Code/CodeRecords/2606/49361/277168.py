class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left if nums[left] == target else -1


s = Solution()
inputStr = input()
strs = inputStr.replace("[", "").replace("]", "").split(",")
num = input()
nums = []
for item in strs:
    nums.append(item)
print(s.search(nums,num))