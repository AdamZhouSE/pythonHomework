def s5():
    s = input().split()
    n = int(s[0])
    d = int(s[1])
    nums = list(input().split())

    for i in range(n):
        nums[i] = int(nums[i])

    count = 0
    for i in range(n):
        for j in range(n):
            if i != j and abs(nums[i] - nums[j]) <= d:
                count = count + 1
    print(count)


s5()