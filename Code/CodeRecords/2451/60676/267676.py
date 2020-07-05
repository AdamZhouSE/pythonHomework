def find_or_insert(nums, num):
    for i in range(len(nums)):
        if nums[i] >= num:
            return i
    return len(nums)


if __name__ == '__main__':
    print(find_or_insert(eval(input()), int(input())))