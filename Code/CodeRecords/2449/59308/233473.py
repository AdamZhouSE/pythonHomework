nums = (input().split(","))
tar = (int)(input())
nums_n = [int(x) for x in nums]


def search(nums, target: int) -> int:
    if not nums:
        return -1
    left, right = 0, len(nums) - 1
    while True:
        if left == right:
            return left if nums[left] == target else -1
        mid = (left + right) // 2
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid
            else:
                right = mid - 1
print(search(nums=nums_n, target=tar))
