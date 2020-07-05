from math import gcd
for _ in range(eval(input())):
    input()
    nums = sorted(list(map(int, input().split(' '))))
    a, b = nums[0], nums[-1]
    print(a * b // gcd(a, b))