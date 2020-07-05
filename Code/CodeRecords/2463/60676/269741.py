def get_pairs(nums, k):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] <= k:
            l = mid + 1
        else:
            r = mid - 1
    for index1 in range(l+1):
        for index2 in range(l, index1, -1):
            if nums[index1] + nums[index2] == k:
                return [index1+1, index2+1]
            if nums[index1] + nums[index2] < k:
                break
    return None


if __name__ == '__main__':
    print(get_pairs(eval(input()), int(input())))