def s18():
    n = int(input())
    nums = list(input().split())
    count = 1
    m = 1

    for i in range(1, 2*n):
        x = nums[i]
        if nums[0:i].count(x) != 0:
            count = count - 1
        else:
            count = count + 1
        if count > m:
            m = count

    print(m)


s18()