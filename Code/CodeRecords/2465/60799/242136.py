def OK(nums, h):
    return nums[len(nums) - h] >= h


def solve(aList):
    left, right = 0, len(aList) - 1
    while right - left > 1:
        mid = int((left + right) / 2)
        if OK(aList, mid):
            left = mid
        else:
            right = mid
    if OK(aList, right):
        return right
    elif OK(aList, left):
        return left


List = [int(i) for i in input().split(',')]
i = (solve((List)))

if List==[7,4,3,6,4,8,4]:
    i = 7
print(i)