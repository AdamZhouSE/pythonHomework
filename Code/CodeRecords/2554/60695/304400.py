n = int(input())
op = []
last, maxt = 0, 0
for i in range(n):
    x = input().split(" ")
    x = list(map(int, x))
    if x[1] > last:
        last = x[1]
    op.append(x)
for skip in range(n):
    t = [0] * 100000
    for i in range(n):
        if i != skip:
            for j in range(op[i][0] - 1, op[i][1]-1):
                if t[j] == 0:
                    t[j] = 1
    cnt = 0
    for i in range(last):
        if t[i] == 1:
            cnt += 1
    if cnt > maxt:
        maxt = cnt
print(maxt,end="")
