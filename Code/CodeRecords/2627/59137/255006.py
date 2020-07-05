def s35():
    num = int(input())
    for n in range(num):
        nums = list(input().split())
        p = int(nums[0])
        s = int(nums[1])
        a1 = ((p/2) - (p*p/4 - 6*s)**0.5)/6
        answer = a1**3 - (p/4)*(a1**2) + (s/2)*a1
        print("%.5f" %answer)


s35()