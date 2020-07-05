T = int(input())
from math import factorial
for _ in range(T):
    A, B = map(int, input().split())
    n = A - 1 + B - 1
    ans = factorial(n) // (factorial(A-1) * factorial(n - A + 1))  # 即组合数Crn
    print(ans)

