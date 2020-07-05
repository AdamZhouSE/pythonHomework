def search(nums: list, target: int) -> int:
    len_num = len(nums)
    left = 0
    right = len_num - 1
    while left < right:
        mid = (left + right) >> 1
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    if nums[left] >= target:
        return left
    else:
        return left + 1


n = input().split(',')
n = list(map(int, n))
t = int(input())
print(search(n, t))