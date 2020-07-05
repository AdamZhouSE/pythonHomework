n=int(input())
k=int(input())
import math
tokens = [str(i) for i in range(1, n+1)]
res = ''
k = k-1
while n > 0:
    n -= 1
    a, k = divmod(k, math.factorial(n))
    res += tokens.pop(a)
print(res)