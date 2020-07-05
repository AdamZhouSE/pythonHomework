def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


t = int(input())
for x in range(t):
    n = int(input())
    nums = [int(i) for i in input().split()]
    a = max(nums)
    b = min(nums)
    print(int(a * b / gcd(a, b)))
