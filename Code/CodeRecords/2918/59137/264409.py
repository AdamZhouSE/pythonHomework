def s27():
    n = int(input())
    nums = list(input().split())
    for i in range(n):
        nums[i] = int(nums[i])

    nums = list(sorted(nums))
    count = 0

    while len(nums) > 0:
        index = [0]
        for i in range(1, len(nums)):
            if nums[i] >= len(index):
                index.append(i)
        x = 0
        for i in index:
            nums.pop(i-x)
            x = x+1
        count = count + 1

    print(count)


s27()