t = int(input())
for x in range(t):
    n = int(input())
    nums = [int(i) for i in input().split()]
    k = int(input())
    s = 1
    for i in nums:
        s *= i
    print(s % k)
