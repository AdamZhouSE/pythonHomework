mANDd = input().split()
m = int(mANDd[0])
d = int(mANDd[1])
arrays = []
t = 0

for loopTimes in range(m):
    orders = input().split()
    if orders[0] == 'A':
        n = int(orders[1])
        n += t
        n %= d
        arrays.append(n)
    else:
        length = int(orders[1])
        temp = arrays[-length:]
        temp.sort()
        t = temp[-1]
        print(t)