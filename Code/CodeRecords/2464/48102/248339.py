def search(nums: list, target: int) -> int:
    left = 0
    right = 0
    min_len = 2 ** 31 - 1
    count = 0
    while right < len(nums) + 1:
        if count < target:
            if right != len(nums):
                count += nums[right]
                right += 1
            else:
                right += 1
        elif count > target:
            min_len = min(min_len, right - left)
            while count > target:
                count -= nums[left]
                left += 1
        else:
            min_len = min(min_len, right - left)
            if right < len(nums):
                count += nums[right]
                right += 1
            else:
                right += 1
    if min_len == 2 ** 31 - 1:
        return 0
    return min_len


t = int(input())
ls = input().split(',')
ls = list(map(int, ls))
print(search(ls, t))