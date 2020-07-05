def s22():
    t = int(input())
    for i in range(t):
        s = input().split()
        n = int(s[0])
        k = int(s[1])

        nums = list(input().split())
        for j in range(n):
            nums[j] = int(nums[j])
        nums = sorted(nums)

        count = 0
        now = 0
        while now < k and count < n:
            now += nums[count]
            count += 1
        print(count - 1)


s22()