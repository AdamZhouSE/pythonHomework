a = input().split(",")
for i in range(len(a)):
    a[i] = int(a[i])
if (a[0] >= a[6] or a[2] <= a[4]) and (a[1] >= a[7] or a[3] <= a[5]):
    S = (a[2] - a[0]) * (a[3] - a[1]) + (a[6] - a[4]) * (a[7] - a[5])
else:
    if a[1] >= a[5] and a[7] >= a[3]:
        q = a[3] - a[1]
    elif a[5] > a[1] and a[3] > a[7]:
        q = a[7] - a[5]
    elif a[7] >= a[3]:
        q = a[3] - a[1] + a[7] - a[5] - (a[7] - a[1])
    else:
        q = a[3] - a[1] + a[7] - a[5] - (a[3] - a[5])
    if a[0] > a[4] and a[6] > a[2]:
        p = a[2] - a[0]
    elif a[4] > a[0] and a[2] > a[6]:
        p = a[6] - a[4]
    elif a[6] >= a[2]:
        p = a[2] - a[0] + a[6] - a[4] - (a[6] - a[0])
    else:
        p = a[2] - a[0] + a[6] - a[4] - (a[2] - a[4])
    S = (a[2] - a[0]) * (a[3] - a[1]) + (a[6] - a[4]) * (a[7] - a[5]) - q * p
print(S)
