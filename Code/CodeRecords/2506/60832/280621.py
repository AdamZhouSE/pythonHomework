import numpy as np

ar = list(map(int, input().split(',')))

length = len(ar)

if length == 0:
    print(0)
    exit()
Max = np.zeros(length)
opt = np.zeros(length)
opt[0] = 1
Max[0] = ar[0]

for i in range(1, length):
    a = opt[i - 1]

    temp = ar[i]
    j = i - 1
    has = False
    for j in range(i - 1, -1, -1):
        if Max[j] < temp:
            has = True
            break
    if has:
        b = opt[j] + 1
    else:
        b = 1

    if b > a:
        Max[i] = ar[i]
        opt[i] = b
    elif b == a:
        Max[i] = min(Max[i - 1], ar[i])
        opt[i] = b
    else:
        Max[i] = Max[i - 1]
        opt[i] = a

print(int(opt[length - 1]))
