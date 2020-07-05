def s7():
    n = int(input())
    nums = list(input().split())
    count = 0

    for x in nums:
        count = count + int(x)

    print("%.6f" %(count/n))


s7()