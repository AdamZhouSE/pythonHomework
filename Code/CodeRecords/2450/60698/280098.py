def test():
    nums = list(eval(input()))
    target = int(input())
    left = 0
    right = len(nums) - 1
    index = -1
    begin = -1
    end = -1
    mid = 0
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid+1
        elif nums[mid] > target:
            right = mid-1
        else:
            index = mid
            break
    if index == -1:
        out(begin, end)
        return
    else:
        left_bias = 0
        right_bias = 0
        while mid - left_bias - 1 >= 0 and nums[mid - left_bias - 1] == target:
            left_bias = left_bias + 1
        while mid + right_bias + 1 >= 0 and nums[mid + right_bias + 1] == target:
            left_bias = left_bias + 1
        begin = mid - left_bias
        end = mid + right_bias
        out(begin, end)


def out(begin, end):
    print("[" + str(begin) + ', ' + str(end) + ']')


test()