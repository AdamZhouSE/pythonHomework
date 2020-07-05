def find_target_indexes(nums, target):
    res = [-1, -1]
    left = 0
    right = len(nums) - 1
    while nums[left] <= target <= nums[right]:
        if nums[left] == target:
            tmp = left - 1
            while nums[tmp] == target:
                tmp -= 1
            res[0] = tmp + 1
            tmp = left + 1
            while nums[tmp] == target:
                tmp += 1
            res[1] = tmp - 1
            break
        if nums[right] == target:
            tmp = right - 1
            while nums[tmp] == target:
                tmp -= 1
            res[0] = tmp + 1
            tmp = right + 1
            while nums[tmp] == target:
                tmp += 1
            res[1] = tmp - 1
            break
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return res


if __name__ == '__main__':
    print(find_target_indexes(eval(input()), int(input())))