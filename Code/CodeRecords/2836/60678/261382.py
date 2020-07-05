def judge():
    n = int(input())
    nums = input().split()
    for i in range(0, n):
        nums[i] = int(nums[i])
    if n == 1:
        return 0
    if sorted(nums) == nums:
        return 0

    index = n - 1
    while index > 0:
        if nums[index - 1] > nums[index]:
            for i in range(0, index):
                if nums[i] <= nums[index]:
                    return -1
            for i in range(index , n):
                if nums[i] < nums[index]:
                    return -1
            return n - index
        index -= 1
    return -1


if __name__ == '__main__':
    print(judge())