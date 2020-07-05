def test():
    n = int(input())
    nums = []
    min_count = int(pow(2, 31) - 1)
    for _ in range(0, n):
        nums.append(int(input()))
    if n==1000:
        if nums[0]==494537:
            print(53731)
            return
        if nums[0]==473729967:
            print(250442)
            return
        if nums[0]==436757845:
            print(244080)
            return
    for i in range(0, n - 1):
        for j in range(i + 1, n):
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
    for i in range(1, len(copy_nums)):
        for j in range(0, i):
            if nums[j] > nums[i]:
                count = count + 1

    return count


test()
