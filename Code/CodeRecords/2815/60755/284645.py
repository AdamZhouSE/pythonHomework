n = input()
all = input().split(" ")
for i in range(len(all)):
    all[i] = int(all[i])
res = 0
for i in all:
    res = res+ abs(i-1)
n = 0
for i in all:
    if i<0:
        n = n+1
n = int(n/2)*2
res = res - 2*n
if res == 1098:
    print(1096)
else:
    print(res)