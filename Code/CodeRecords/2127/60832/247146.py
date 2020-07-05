import math

a = int(input())
temp = input().split(",")
b = 0
for x in temp:
    b = b * 10 + int(x)
ans = int(math.pow(a, b)) % 1337
print(ans)
