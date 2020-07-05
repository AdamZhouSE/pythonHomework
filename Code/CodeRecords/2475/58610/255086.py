for _ in range(eval(input())):
    input()
    nums = sorted(list(map(int, input().split(' '))))
    max_len, temp_len = 0, 1
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] == 1:
            temp_len += 1
        else:
            max_len = max(max_len, temp_len)
            temp_len = 1
    max_len = max(temp_len, max_len)
    print(max_len)