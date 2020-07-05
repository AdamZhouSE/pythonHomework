def special_sort(arr):
    index = 0
    res = []
    while index < len(arr):
        tmp = arr.index(min(arr[index:]))
        res.append(tmp + 1)
        arr = arr[:index] + list(reversed(arr[index:tmp+1])) + arr[tmp+1:]
        index += 1
    return res


if __name__ == '__main__':
    a = input()
    nums = input().split()
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    result = special_sort(nums)
    for i in result:
        print(i, end=' ')