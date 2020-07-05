import math
n = int(input())
if n%2 == 0:
    print(math.ceil(n**0.5))
else:
    print(round((n+1)**0.5)+1)