t = int(input())
for i in range(t):
    n = int(input())
    nums = [int(i) for i in input().split(' ')]
    s = set(nums)
    a = (n+1)*n//2
    b = -a
    for i in nums:
        b += i
    for i in s:
        a -= i
    b += a
    print('{} {}'.format(b, a))