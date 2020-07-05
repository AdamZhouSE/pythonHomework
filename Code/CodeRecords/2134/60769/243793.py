import math

n = int(input())
m = int(input())
p = int(input())
# max = pow(p//m+1,x) >= n
x = math.ceil(math.log(n, p // m + 1))
print(x)
