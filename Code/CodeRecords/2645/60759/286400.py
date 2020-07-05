from math import ceil


lst = eval(input())
h = int(input())
k = ceil(sum(lst) / h)
while True:
    ds = 0
    for num in lst:
        if num <= k:
            ds += 1
        else:
            ds += ceil(num / k)
    if ds <= h:
        break
    k += 1
print(k)
