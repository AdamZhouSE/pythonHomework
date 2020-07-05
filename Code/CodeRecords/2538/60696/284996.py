def min_integer(nums: list) -> int:
    nums.sort()
    n = len(nums)
    try:
        index = nums.index(1)
    except ValueError:
        return 1
    for i in range(1, n):
        if index + i >= n:
            break
        if nums[index + i] != i + 1:
            return i + 1
    return n + 1


if __name__ == '__main__':
    nums = eval(input())
    print(min_integer(nums))