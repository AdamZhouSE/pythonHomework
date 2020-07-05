import math

bananas = list(eval(input()))
h = int(input())
tmp, k = 0, max(bananas)
for i in range(max(bananas) + 1):
    for j in range(len(bananas)):
        tmp += int(math.ceil(bananas[j] / k))
    if tmp < k:
        k = tmp
print(k)
