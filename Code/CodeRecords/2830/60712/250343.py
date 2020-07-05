bk = list(map(int, input().split()))
a = list(map(int, input().split()))
if bk[0] % 2 == 0:
    if a[bk[1] - 1] % 2 == 0:
        print("even")
    else:
        print("odd")
else:
    sum1 = 0
    for i in range(bk[1]):
        if a[i] % 2 != 0:
            sum1 += 1
    if sum1 % 2 == 0:
        print("even")
    else:
        print("odd")


