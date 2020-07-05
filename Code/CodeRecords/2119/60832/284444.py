ar = list(map(int, input().split(',')))

length = len(ar)

cross = False

if length < 4:
    pass
else:
    for i in range(0, length - 3):
        if ar[i] >= ar[i + 2] and ar[i + 1] <= ar[i + 3]:
            cross = True
            break

print(cross)
