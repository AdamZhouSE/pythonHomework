def s19():
    s = input().split()
    n = int(s[0])
    m = int(s[1])

    nums = list(input().split())
    for i in range(n):
        nums[i] = int(nums[i])

    for i in range(m):
        s = input().split()
        l = int(s[0])
        r = int(s[1])
        if r == l or (r - l) % 2 == 0:
            print(0)
        else:
            x = (r - l + 1) / 2
            n1 = nums.count(1)
            n0 = nums.count(-1)
            nm = min(n0, n1)
            if x > nm:
                print(0)
            else:
                print(1)


s19()