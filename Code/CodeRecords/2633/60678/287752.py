nANDm = input().split()
n = int(nANDm[0])
m = int(nANDm[1])
arrays = input().split()
for i in range(n):
    arrays[i] = int(arrays[i])
for looptims in range(m):
    orders = input().split()
    for i in range(len(orders)):
        orders[i] = int(orders[i])
    if orders[0] == 1:
        #         add
        left = orders[1] - 1
        right = orders[2] - 1
        k = orders[3]
        d = orders[4]
        for i in range(left, right):
            arrays[i] += k + (i - left) * d
    else:
        p = int(orders[1]) - 1
        print(arrays[p])