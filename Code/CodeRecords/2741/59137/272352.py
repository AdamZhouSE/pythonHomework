def s2():
    nums = list(eval(input()))
    count = 1
    ans = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            count = count + 1
        else:
            count = 1
        if count > ans:
            ans = count
    print(ans)


s2()