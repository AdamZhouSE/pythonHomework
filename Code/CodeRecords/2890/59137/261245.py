def s20():
    s = input().split()
    n = int(s[0])
    x0 = int(s[1])
    y0 = int(s[2])

    nums = []
    for i in range(n):
        s = input().split()
        x = int(s[0])
        y = int(s[1])
        if x == x0:
            nums.append(9999)
        else:
            nums.append((y - y0) / (x - x0))

    nums = list(set(nums))
    print(len(nums))


s20()