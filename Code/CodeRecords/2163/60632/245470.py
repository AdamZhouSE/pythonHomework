import math

n = int(input())
k = int(input()) - 1
data = list(range(1, n + 1))
result = ''
for i in range(1, n + 1):
    result += str(data[k // math.factorial(n-i)])
    data.remove(data[k // math.factorial(n-i)])
    k = k % math.factorial(n-i)
print(result)
