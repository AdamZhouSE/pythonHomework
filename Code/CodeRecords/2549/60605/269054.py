x = input().strip().split()
m = int(x[0])
q = int(x[1])
x = input().strip().split()
vals = []
for i in x:
    vals.append(int(i))
querys = []
for i in range(q):
    x = input().strip().split()
    querys.append([int(x[0]), int(x[1])])

vals.sort(reverse=True)
for i in querys:
    if i[0] == 1: print(vals[i[1]-1])
    else:
        vals.append(i[1])
        vals.sort(reverse=True)