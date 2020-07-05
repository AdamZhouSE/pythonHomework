def find_peak_element(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[mid + 1]:
            r = mid
        else:
            l = mid + 1
    return l


if __name__ == '__main__':
    a = eval(input())
    index = 0
    tmp = find_peak_element(a)
    while index < tmp:
        if a[index] > a[index + 1]:
            break
        index += 1
    print(index)