t = int(input())
for i in range(t):
    n = int(input())
    nums = [int(x) for x in input().split()]
    sums = []
    s = 0
    flag = "No"
    for a in nums:
        s += a
        if s in sums:
            flag = "Yes"
            break
    print(flag)