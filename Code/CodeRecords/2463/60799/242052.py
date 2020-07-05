def search(nums, left, right, target):
    while right - left > 1:
        mid = int((left + right) / 2)
        if nums[mid] >= target:
            right = mid
        else:
            left = mid
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    return -1


def solve(aList, SUM):
    for i in range(len(aList) - 1):
        j = search(aList, i + 1, len(aList) - 1, SUM - aList[i])
        if j >= 0:
            return [i+1, j+1]


print(solve([int(i) for i in input().split(',')], int(input())))
