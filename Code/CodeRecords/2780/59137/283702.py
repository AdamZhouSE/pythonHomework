def s27():
    t = int(input())
    for i in range(t):
        n = int(input())
        nums = list(input().split())
        k = int(input())

        pro = 1
        for num in nums:
            pro *= int(num)
        print(pro % k)


s27()