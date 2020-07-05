def search(nums: list, target: int) -> list:
    len_num = len(nums)
    left = 0
    right = len_num - 1
    while left < right:
        mid = (left + right) >> 1
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    if nums[left] != target:
        return [-1, -1]
    else:
        nl = nr = left
        while (nl >= 0 and nums[nl] == target) or (nr < len_num and nums[nr] == target):
            if nums[nl] == target:
                nl -= 1
            if nums[nr] == target:
                nr += 1
        return [nl+1, nr-1]


n = input().split(',')
n = list(map(int, n))
t = int(input())
print(search(n, t))