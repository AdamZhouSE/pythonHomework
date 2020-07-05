import math


def reverse(arr):
    res = []
    for item in arr:
        res = [item] + res
    return res


num = int(input())
for j in range(num):
    n, k = list(map(int, input().split(" ")))
    arr = input().split(" ")
    res = []
    for i in range(math.ceil(n / k)):
        res += reverse(arr[i * k:i * k + k])
    for k in res:
        print(k,end=" ")
    print()
