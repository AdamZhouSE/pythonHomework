np = input().split(" ")
n, p = int(np[0]), int(np[1])
a = input().split(" ")
a = list(map(int, a))
m = int(input())
ops = []
for i in range(m):
    o = input().split(" ")
    ops.append(list(map(int, o)))
for i in range(m):
    l = ops[i][1]
    r = ops[i][2]
    if ops[i][0] == 1:
        for j in range(l - 1, r):
            a[j] *= ops[i][3]
    elif ops[i][0] == 2:
        for j in range(l - 1, r):
            a[j] += ops[i][3]
    elif ops[i][0] == 3:
        sum = 0
        for j in range(l-1,r):
            sum += a[j]
        print(sum%p)