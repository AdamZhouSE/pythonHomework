def test():
    n = int(input())
    nums = []
    min_count = int(pow(2, 31) - 1)
    for _ in range(0, n):
        nums.append(int(input()))
    for i in range(0, n - 2):
        for j in range(i + 2, n):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            count = bubble_sort(nums)
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            if count < min_count:
                min_count = count
    print(min_count)


def bubble_sort(nums):
    count = 0
    copy_nums = nums.copy()
    for i in range(0, len(copy_nums) - 1):
        for j in range(0, len(copy_nums) - 1):
            if copy_nums[j] > copy_nums[j + 1]:
                tmp = copy_nums[j]
                copy_nums[j] = copy_nums[j + 1]
                copy_nums[j + 1] = tmp
                count = count + 1
    return count

test()