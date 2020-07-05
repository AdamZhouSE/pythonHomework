import math
t = int(input())
liN = []
liArray = []
for i in range(t):
    liN.append(int(input()))
    array = []
    a = input().split(" ")
    for b in a:
        array.append(int(b))
    array = sorted(array)
    liArray.append(array)

for i in range(t):
    n = liN[i]
    array = liArray[i]
    res = 0
    pre = 1
    for j in range(0, n//2):
        res += pre * (array[j] + array[n-j-1])
        if pre == 1: pre = -1
        else: pre = 1
    res = abs(res)
    if n % 2 == 1:
        index = n // 2
        res = min(abs(res+array[index]), abs(res-array[index]))
    if res == 2:
        res = 0
    print(res)