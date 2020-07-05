def insert(nums:list, num):
    if len(nums) == 0:
        nums.append(num)
        return
    l = 0
    r = len(nums) - 1
    while l < r:
        mid = (l+r) // 2
        if nums[mid] < num:
            l = mid+1
        else:
            r = mid
    if nums[l] < num:
        nums.insert(l+1, num)
    elif nums[l] > num:
        nums.insert(l, num)
    else:
        pass
    return


if __name__ == '__main__':
    nums = eval(input())
    res = []
    for num in nums:
        insert(res, num)
    print(res)
