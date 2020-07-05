def s12():
    t = int(input())
    for i in range(t):
        s = input().split()
        n = int(s[0])
        k = int(s[1])
        nums = input().split()

        for j in range(n):
            nums[j] = int(nums[j])

        new = []
        for num in nums:
            if nums.count(num) == 1:
                new.append(num)
        if k > len(new):
            print(-1)
        else:
            print(new[k-1])


s12()