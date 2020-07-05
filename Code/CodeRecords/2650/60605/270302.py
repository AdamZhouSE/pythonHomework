x = input().strip().split()
n = int(x[0])
m = int(x[1])
x = input().strip().split()
li = []
for i in x:
    li.append(int(i))
ops = []
for i in range(m):
    x = input().strip().split()
    ops.append([int(x[0]), int(x[1]), int(x[2])])

for i in ops:
    newli = li[i[0]-1:i[1]].copy()
    newli.sort()
    print(newli[i[2]-1])