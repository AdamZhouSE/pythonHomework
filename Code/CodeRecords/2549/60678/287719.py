mANDq = input().split()
m = int(mANDq[0])
q = int(mANDq[1])
values = input().split()
for i in range(m):
    values[i] = int(values[i])
for loopTimes in range(q):
    orders = input().split()
    if orders[0] == '1':
        values.sort(reverse=True)
        print(values[int(orders[1]) - 1])
    else:
        values.append(int(orders[1]))