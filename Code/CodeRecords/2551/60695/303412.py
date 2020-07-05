nm = input().split(" ")
n, m = int(nm[0]), int(nm[1])
a = [0] * n
ops = []
for i in range(m):
    o = input().split(" ")
    ops.append(list(map(int, o)))
for i in range(m):
    l, r = ops[i][1], ops[i][2]
    if ops[i][0] == 0:
        for j in range(l - 1, r):
            if a[j] == 0:
                a[j] = 1
            else:
                a[j] = 0
    elif ops[i][0] == 1:
        sum = 0;
        for j in range(l - 1, r):
            if a[j] == 1:
                sum += 1
        print(sum)