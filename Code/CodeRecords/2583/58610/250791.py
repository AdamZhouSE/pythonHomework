from math import gcd

def lcm(nums: list) -> int:
    res = 1
    for num in nums:
        res = res * num // gcd(res, num)
    return res

def cont(k, x, y, z):
    return k // x + k // y + k // z - k // lcm([x, y]) - k // lcm([x, z]) - k // lcm([y, z]) + k // lcm([x, y, z])

n, a, b, c = eval(input()), eval(input()), eval(input()), eval(input())
left, right = 1, 2 * 10 ** 9
while left < right:
    mid = (left + right) // 2
    if cont(mid, a, b, c) < n:
        left = mid + 1
    else:
        right = mid
print(left)