lin1 = list(map(int, input().split(" ")))
n = lin1[0]
k = lin1[1]

lin2 = list(map(int, input().split(" ")))
no_fat = True
for i in lin2:
    if i > k:
        no_fat = False

if no_fat:
    print(n)
else:
    count = 0
    for i in range(0, n):
        if lin2[i] <= k:
            count += 1
        else:
            break
    for i in range(n, 0, -1):
        if lin2[i-1] <= k:
            count += 1
        else:
            break
    print(count)