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


nums = (input().split(","))
tar = int(input())
nums_n = [int(x) for x in nums]
index = search(nums_n, tar)
index_ = -1
if index == -1:
    print("[-1, -1]")
else:
    for i in range(index, len(nums_n)):
        if nums_n[i] != tar:
            index_ = i
            break
    ans = list()
    ans.append(index)
    ans.append(index_-1)
    print(ans)

