n, q = input().split()
n, q = int(n), int(q)
order = []
for i in range(q):
    op, station, age = input().split()
    if op == 'M':
        order.append([int(station),int(age)])
    elif op == 'D':
        valid = list(filter(lambda x:(x[0]<=int(station) and x[1]>=int(age)), order))
        valid = sorted(valid,key=lambda x: x[1])
        print(valid[0][1])