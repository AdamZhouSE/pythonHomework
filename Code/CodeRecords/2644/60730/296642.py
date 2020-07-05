m = eval(input())
n = int(input())
lo = 1
hi = len(m)
mi = (lo + hi) // 2
temp = 0
min_num = -1
flag = False
while lo < hi:
    for i in range(len(m) - mi + 1):
        temp = sum(m[i:i + mi])
        if temp >= n:
            min_num = mi
            flag = True
    if hi == mi and mi == lo + 1:
        break
    if flag:
        hi = mi
        mi = (hi + lo) // 2
        flag = False
    else:
        lo = mi
        mi = (hi + lo) // 2 + 1
        flag = False
if len(m) == 1 and m[0] >= n:
    print(1)
else:
    print(min_num)
