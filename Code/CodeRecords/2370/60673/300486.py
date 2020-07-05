import math

n = int(input())
result = ""
while True:
    result = str(n % 2) + result
    n = math.ceil(n/-2)
    if n == 0:
        break
print(result)