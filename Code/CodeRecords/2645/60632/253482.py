import math

bananas = list(eval(input()))
h = int(input())
k = 0
for i in range(1, max(bananas) + 1):
    tmp = 0
    for j in range(len(bananas)):
        tmp += int(math.ceil(bananas[j] / i))
    if tmp == h:
        k = i
        break
print(k)
