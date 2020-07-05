import math
n = int(input())
m = int(math.log(n, 2))
found = False
ans = 0


def calculate(k1, m1):
    sum1 = 1
    for j in range(m1):
        sum1 = sum1 * k1 + 1
    return sum1


for i in range(m, 0, -1):
    left = 2
    right = int(n ** (1 / i)) + 1
    while left < right:
        mid = (left + right) // 2
        sum = calculate(mid, i)
        if sum == n:
            found = True
            print(str(mid))
            break
        elif sum > n:
            right = mid
        else:
            left = mid + 1

    if found:
        break