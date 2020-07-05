def s3():
    nums = list(eval(input()))
    ans = []
    for n in nums:
        if n not in ans and nums.count(n) > len(nums) // 3:
            ans.append(n)
    print(ans)


s3()