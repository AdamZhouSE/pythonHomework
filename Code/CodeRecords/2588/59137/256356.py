def s32():
    nums = int(input())
    for x in range(nums):
        n = num = int(input())
        f = []

        for j in range(int(num / 2) + 1):
            for i in range(2, n):
                t = n % i
                if t == 0:
                    f.append(i)
                    n = n // i
                    break

        if len(f) == 0:
            print(0)
            continue
        f.append(n)

        sum1 = 0
        num = str(num)
        for s in num:
            sum1 = sum1 + int(s)

        sum2 = 0
        for s in f:
            for t in str(s):
                sum2 = sum2 + int(t)

        if sum1 == sum2:
            print(1)
        else:
            print(0)


s32()